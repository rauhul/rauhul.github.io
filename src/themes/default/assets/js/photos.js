var photo_overlay = undefined;
var photo_overlay_image = undefined;

document.addEventListener("DOMContentLoaded", function(event) {
	photo_overlay = document.querySelectorAll('.photo-overlay')[0];
	photo_overlay_image = document.querySelectorAll('.photo-overlay-image')[0];
	
	photo_overlay.addEventListener('click', (event) => {
		document.startViewTransition(() => {
			photo_overlay.classList.toggle('hidden');
		});
	});

	let photos = document.querySelectorAll('.photo-image');
	photos.forEach(function(photo) {
		let src = photo.getAttribute('src').split('?')[0];
		photo.addEventListener('click', (event) => {
			document.startViewTransition(() => {
				photo_overlay_image.setAttribute('src', src);
				photo_overlay.classList.toggle('hidden');
			});
		});
	});
});
