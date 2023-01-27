// Select the animated text element
const animatedText = document.querySelector('.animated-text');

// Create an observer for the animated text element
const observer = new IntersectionObserver((entries) => {
    // Check if the animated text element is in the viewport
    if (entries[0].isIntersecting) {
        // Add the "visible" class to the animated text element
        animatedText.classList.add('visible');
    } else {
        // Remove the "visible" class from the animated text element
        animatedText.classList.remove('visible');
    }
});

// Start observing the animated text element
observer.observe(animatedText);
