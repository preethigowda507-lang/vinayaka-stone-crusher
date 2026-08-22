document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    const menuToggle =
        document.getElementById("menuToggle");

    const mainNav =
        document.getElementById("mainNav");


    if (menuToggle && mainNav) {

        menuToggle.addEventListener("click", function () {

            mainNav.classList.toggle("show");

        });

    }


    /* =====================================================
       CLOSE MOBILE MENU
    ===================================================== */

    const navLinks =
        document.querySelectorAll("#mainNav a");


    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            if (mainNav) {

                mainNav.classList.remove("show");

            }

        });

    });


    /* =====================================================
       COPYRIGHT YEAR
    ===================================================== */

    const yearElement =
        document.getElementById("year");


    if (yearElement) {

        yearElement.textContent =
            new Date().getFullYear();

    }


    /* =====================================================
       SCROLL REVEAL
    ===================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");


    if ("IntersectionObserver" in window) {

        const revealObserver =
            new IntersectionObserver(
                function (entries, observer) {

                    entries.forEach(function (entry) {

                        if (entry.isIntersecting) {

                            entry.target.classList.add("active");

                            observer.unobserve(
                                entry.target
                            );

                        }

                    });

                },
                {
                    threshold: 0.10
                }
            );


        revealElements.forEach(function (element) {

            revealObserver.observe(element);

        });

    } else {

        revealElements.forEach(function (element) {

            element.classList.add("active");

        });

    }


    /* =====================================================
       NAVBAR SCROLL
    ===================================================== */

    const navbar =
        document.querySelector(".navbar");


    window.addEventListener("scroll", function () {

        if (!navbar) {
            return;
        }


        if (window.scrollY > 50) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    });


    /* =====================================================
       PHONE NUMBER
       ALLOW ONLY NUMBERS
    ===================================================== */

    const phoneInputs =
        document.querySelectorAll(
            'input[type="tel"]'
        );


    phoneInputs.forEach(function (input) {

        input.addEventListener("input", function () {

            input.value =
                input.value.replace(/\D/g, "")
                           .slice(0, 10);

        });

    });


    /* =====================================================
       FORM SUBMIT BUTTON
    ===================================================== */

    const forms =
        document.querySelectorAll("form");


    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const button =
                form.querySelector(
                    'button[type="submit"]'
                );


            if (button) {

                button.textContent =
                    "Submitting...";

                button.disabled = true;

            }

        });

    });

});