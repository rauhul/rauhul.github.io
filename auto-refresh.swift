import Foundation
import CoreServices

let filePath = "/Users/rauhul/Developer/rauhul/rauhul.github.io/docs/index.html"
let directoryPath = URL(fileURLWithPath: filePath).deletingLastPathComponent().path

// Callback function for file system events
let eventCallback: FSEventStreamCallback = { _, _, numEvents, eventPaths, eventFlags, _ in
    guard let eventPaths = unsafeBitCast(eventPaths, to: UnsafeMutablePointer<CFArray>?.self),
          let paths = unsafeBitCast(CFArrayGetValueAtIndex(eventPaths.pointee, 0), to: CFString.self) as String?
    else { return }

    if paths == filePath {
        print("File change detected at: \(paths)")

        let script = """
        tell application "Safari"
            do JavaScript "window.location.reload()" in front document
        end tell
        """

        var error: NSDictionary?
        if let scriptObject = NSAppleScript(source: script) {
            print("Executing AppleScript to refresh Safari.")
            scriptObject.executeAndReturnError(&error)
        } else {
            print("Failed to create AppleScript object.")
        }

        if let error = error {
            print("AppleScript Error: \(error)")
        } else {
            print("Safari refreshed successfully.")
        }
    }
}

// Create an event stream
var context = FSEventStreamContext(version: 0, info: nil, retain: nil, release: nil, copyDescription: nil)
let eventStream = FSEventStreamCreate(
    kCFAllocatorDefault,
    eventCallback,
    &context,
    [directoryPath] as CFArray,
    FSEventStreamEventId(kFSEventStreamEventIdSinceNow),
    0.5, // Latency in seconds (adjust as needed)
    FSEventStreamCreateFlags(kFSEventStreamCreateFlagFileEvents | kFSEventStreamCreateFlagUseCFTypes)
)

if let eventStream = eventStream {
    if let runLoop = CFRunLoopGetCurrent() {
        FSEventStreamScheduleWithRunLoop(eventStream, runLoop, CFRunLoopMode.defaultMode.rawValue)
        FSEventStreamStart(eventStream)

        print("Started monitoring \(filePath) for changes.")
        CFRunLoopRun() // Keep the program running
    } else {
        print("Error: Failed to get the current run loop.")
    }
} else {
    print("Failed to create FSEventStream.")
}
