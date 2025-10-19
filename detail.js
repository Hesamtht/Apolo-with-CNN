// Animate font
document.addEventListener("DOMContentLoaded", function() {
    animateFont();
});

function animateFont() {
    const title = document.querySelector('.display-4');
    let letters = title.textContent.split('');
    title.textContent = ''; // Clear title content
    letters.forEach(function(letter, index) {
        let span = document.createElement('span');
        span.textContent = letter;
        span.style.animationDelay = `${index * 0.1}s`;
        title.appendChild(span);
    });
}
