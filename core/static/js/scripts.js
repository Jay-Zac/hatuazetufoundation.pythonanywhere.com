window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });


});

//form submission
const form = document.getElementById("form");
form.addEventListener('submit', submitHandler);

function submitHandler(e) {
    e.preventDefault();
    fetch(form.action, {
        method: 'POST',
        body: new FormData(form)
    })
    .then(response => response.json())
    .then(data => {
        if(data.message === 'success') {
            alert('Your Message was submitted Successfully!')
            form.reset()
        }
    })
    }

// Get the back-to-top button
const backToTop = document.getElementById('back-to-top');

// Hide the button when the user is at the top of the page
window.addEventListener('scroll', () => {
    if (window.scrollY === 0) {
        backToTop.style.display = 'none';
    } else {
        backToTop.style.display = 'block';
    }
});

// Hide the button after a delay when the user scrolls up or down
let lastScrollY = 0;
window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    if (currentScrollY > lastScrollY) {
        setTimeout(() => {
            backToTop.style.display = 'none';
        }, 5000);
    } else if (currentScrollY < lastScrollY) {
        setTimeout(() => {
            backToTop.style.display = 'none';
        }, 5000);
    }
    lastScrollY = currentScrollY;
});

// Show the button when the user touches the screen
document.addEventListener('touchstart', () => {
    backToTop.style.display = 'block';
});