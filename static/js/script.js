document.addEventListener(
    "DOMContentLoaded",
    function () {


        // ==========================================
        // NAVBAR SCROLL
        // ==========================================

        const navbar =
            document.querySelector(".navbar");


        window.addEventListener(
            "scroll",
            function () {

                if (!navbar) {
                    return;
                }


                if (window.scrollY > 50) {

                    navbar.classList.add(
                        "scrolled"
                    );

                } else {

                    navbar.classList.remove(
                        "scrolled"
                    );

                }

            }
        );


        // ==========================================
        // PHONE VALIDATION
        // ==========================================

        const phone =
            document.getElementById("phone");


        if (phone) {

            phone.addEventListener(
                "input",
                function () {

                    this.value =
                        this.value.replace(
                            /[^0-9]/g,
                            ""
                        );

                }
            );

        }


        // ==========================================
        // FORM SUBMIT
        // ==========================================

        const form =
            document.getElementById(
                "contactForm"
            );


        if (form) {

            form.addEventListener(
                "submit",
                function () {

                    const button =
                        form.querySelector(
                            ".submit-btn"
                        );


                    if (button) {

                        button.disabled = true;

                        button.textContent =
                            "Sending Request...";

                    }

                }
            );

        }


        // ==========================================
        // REVEAL ANIMATION
        // ==========================================

        const revealElements =
            document.querySelectorAll(
                ".card, .material-card, .gallery-item, .truck-card"
            );


        const observer =
            new IntersectionObserver(
                function (entries) {

                    entries.forEach(
                        function (entry) {

                            if (entry.isIntersecting) {

                                entry.target.classList.add(
                                    "visible"
                                );

                            }

                        }
                    );

                },
                {
                    threshold: 0.12
                }
            );


        revealElements.forEach(
            function (element) {

                observer.observe(element);

            }
        );

    }
);
document.addEventListener("DOMContentLoaded", function () {

    // Smooth page loading
    document.body.classList.add("page-loaded");


    // Animate cards when they enter the screen
    const cards = document.querySelectorAll(
        ".material-card, .feature-card, .gallery-card, .truck-card"
    );

    const observer = new IntersectionObserver(
        function (entries) {

            entries.forEach(function (entry) {

                if (entry.isIntersecting) {

                    entry.target.classList.add("show");

                    observer.unobserve(entry.target);
                }

            });

        },
        {
            threshold: 0.12
        }
    );


    cards.forEach(function (card) {
        observer.observe(card);
    });


    // Prevent accidental empty form submissions
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const button = form.querySelector(
                'button[type="submit"]'
            );

            if (button) {
                button.innerText = "Sending...";
                button.disabled = true;
            }

        });

    });

});