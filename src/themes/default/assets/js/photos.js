var images = [];
var active = undefined
var photo_overlay = undefined;
var photo_overlay_image = undefined;

function startViewTransition(callback) {
  	if (!document.startViewTransition) {
    	callback();
    	return;
  	}

	document.startViewTransition(() => {
		callback();
	});
}

function updateActivePhoto(index) {
	active = index;
	if (active != undefined) {
		photo_overlay_image.setAttribute('src', images[active]);
		photo_overlay.classList.remove('hidden');
	} else {
		photo_overlay.classList.add('hidden');
		photo_overlay_image.removeAttribute('src');
	}
}

function mod(n, m) {
	return ((n % m) + m) % m;
}

function previousPhoto() {
	if (active != undefined) { 
		updateActivePhoto(mod(active - 1, images.length));
	}
}

function nextPhoto() {
	if (active != undefined) { 
		updateActivePhoto(mod(active + 1, images.length));
	}
}

function toggleFullScreen() {
	if (active != undefined) { 
		if (!document.fullscreenElement) {
			photo_overlay_image.requestFullscreen();
		} else if (document.exitFullscreen) {
			document.exitFullscreen();
		}
	}
}

document.addEventListener("DOMContentLoaded", function(event) {
	photo_overlay = document.querySelectorAll('.photo-overlay')[0];
	photo_overlay_image = document.querySelectorAll('.photo-overlay-image')[0];
	
	photo_overlay.addEventListener('click', (event) => {
		console.log("clicked:", photo_overlay);
		startViewTransition(() => {
			updateActivePhoto(undefined);
		});
	});

	let photos = document.querySelectorAll('.photo-image');
	photos.forEach(function(element, index) {
		let src = element.getAttribute('src').split('?')[0];
		images.push(src);
		element.addEventListener('click', (event) => {
			startViewTransition(() => {
				updateActivePhoto(index);
			});
		});
	});

	let previous = document.querySelectorAll('.photo-overlay-control-previous');
	previous.forEach(function(element) {
		element.addEventListener('click', (event) => {
			event.stopPropagation();
			previousPhoto();
		});
	});

	let next = document.querySelectorAll('.photo-overlay-control-next');
	next.forEach(function(element) {
		element.addEventListener('click', (event) => {
			event.stopPropagation();
			nextPhoto();
		});
	});
});

document.addEventListener('keydown', (event) => {
	switch (event.key) {
	case 'ArrowLeft':
		previousPhoto();
		break;
	case 'ArrowRight':
		nextPhoto();
		break;
	case 'Enter':
		toggleFullScreen();
		break;
	}
});
