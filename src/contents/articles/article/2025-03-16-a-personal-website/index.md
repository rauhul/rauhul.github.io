---
type: article
title: "A personal website"
description: "Introducing a new rauhul.me, why I built it, and how to enable the CSS features it depends on."
publication: 2025-03-15 14:55:00
tags: 
    - self
---

<!-- I've long thought about building a website, a number of my college friends had their own  -->


## Enabling Grid 3 Support

This site is best viewed with CSS "Grid3" support enabled. Grid3 is an experimental feature that allows for easy  masonry/waterfall layouts popularized by sites like Pinterest, to learn more check out ["Help us invent CSS Grid Level 3, aka “Masonry” layout"](https://webkit.org/blog/15269/help-us-invent-masonry-layouts-for-css-grid-level-3/) by [Jen Simmons](https://bsky.app/profile/jensimmons.bsky.social) on behalf of the WebKit team.

### Safari

#### macOS

If you're using Safari on macOS, this feature can be enabled by first enabling Web Developer features via:

```txt
Safari > Preferences > Advanced > Show features for web developers
```

Then turning on the feature flag via:

```txt
Safari > Preferences > Feature Flags > CSS Masonry Layout
```

#### iOS

If you're using Safari on iOS, this feature can be enabled by turning on the feature flag via:

```txt
Settings > Apps > Safari > Advanced > Feature Flags > CSS Masonry Layout
```

### Firefox

If you're using Firefox, this feature can be enabled by turning on the feature flag via:

```txt
about:config > layout.css.grid-template-masonry-value.enabled
```

You may need to restart Firefox for the setting to take effect.

### Chrome

I'm not currently aware of a way to enable "Grid3" support in Chrome or Chromium based browers, if you happen to know a solution please drop me a line using of my contact methods listed under [links](/links).
