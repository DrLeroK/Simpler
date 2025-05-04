document.addEventListener('DOMContentLoaded', function() {
    // Activate current nav link
    const currentUrl = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade');
            setTimeout(() => alert.remove(), 150);
        }, 5000);
    });

    // Add hover animation to cards
    document.querySelectorAll('.card').forEach(card => {
        card.classList.add('animate-hover');
    });

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});






document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations when elements come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate__animated');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (elementPosition < screenPosition) {
                const animationClass = element.classList.item(1); // Get the animation class
                element.classList.add(animationClass);
            }
        });
    };
    
    // Run on load and scroll
    animateOnScroll();
    window.addEventListener('scroll', animateOnScroll);
    
    // Add hover class to elements
    document.querySelectorAll('.hover-effect').forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.classList.add('animate__pulse');
        });
        element.addEventListener('mouseleave', function() {
            this.classList.remove('animate__pulse');
        });
    });
});




// test page
document.addEventListener('DOMContentLoaded', function() {
    // Add hover animations
    const cards = document.querySelectorAll('.group-card, .post-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Animate sections as they come into view
    const animateOnScroll = function() {
        const sections = document.querySelectorAll('.dashboard-section');
        const windowHeight = window.innerHeight;
        
        sections.forEach((section, index) => {
            const sectionPosition = section.getBoundingClientRect().top;
            const animationDelay = index * 100;
            
            if (sectionPosition < windowHeight * 0.8) {
                section.style.animationDelay = `${animationDelay}ms`;
                section.classList.add('animate-section');
            }
        });
    };
    
    // Run on load and scroll
    window.addEventListener('load', animateOnScroll);
    window.addEventListener('scroll', animateOnScroll);
});





// Thank you page
document.addEventListener('DOMContentLoaded', function() {
    // Add animation class to content
    const thanksContent = document.querySelector('.logout-thanks-content');
    
    // Trigger animation after short delay
    setTimeout(() => {
        thanksContent.classList.add('animate__animated', 'animate__fadeInUp');
    }, 100);
    
    // Add hover effects to buttons
    const buttons = document.querySelectorAll('.btn-login-again, .btn-go-home');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.classList.add('animate__animated', 'animate__pulse');
        });
        
        button.addEventListener('mouseleave', function() {
            this.classList.remove('animate__animated', 'animate__pulse');
        });
    });
    
    // Add confetti effect on page load (optional)
    setTimeout(() => {
        if (typeof confetti === 'function') {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    }, 500);
});




















