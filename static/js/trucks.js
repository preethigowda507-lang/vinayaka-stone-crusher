document.addEventListener("DOMContentLoaded", function () {

    const truckImages = {

        "10wheel": [
            "front.png",
            "side_left.png",
            "back.png",
            "side_right.png",
            "front.png"
        ],

        "6wheel18": [
            "front.png",
            "side_left.png",
            "back.png",
            "side_right.png",
            "front.png"
        ],

        "6wheel14": [
            "front.png",
            "side_left.png",
            "back.png",
            "side_right.png",
            "front.png"
        ],

        "12wheel": [
            "front.png",
            "side_left.png",
            "back.png",
            "side_right.png",
            "front.png"
        ],

        "709": [
            "front.png",
            "side_right.png",
            "back.png",
            "side_left.png",
            "angled.png",
            "front.png"
        ]

    };


    const truckFolders = {

        "10wheel":
            "10wheel",

        "6wheel18":
            "6wheel_LP",

        "6wheel14":
            "6wheel_SC",

        "12wheel":
            "12wheel",

        "709":
            "709"

    };


    const viewerStates = {};


    document.querySelectorAll(".truck-viewer").forEach(function (viewer) {

        const truckName = viewer.dataset.truck;

        if (!truckImages[truckName]) {
            return;
        }

        const image = viewer.querySelector(".truck-photo");

        if (!image) {
            return;
        }

        viewerStates[truckName] = {
            index: 0,
            timer: null
        };


        function showImage(index) {

            const images = truckImages[truckName];

            viewerStates[truckName].index =
                (index + images.length) % images.length;

            const filename =
                images[viewerStates[truckName].index];

            image.style.opacity = "0";

            setTimeout(function () {

                image.src =
                    `/static/trucks/${truckFolders[truckName]}/${filename}`;

                image.style.opacity = "1";

            }, 150);

        }


        viewer.showNext = function () {

            showImage(
                viewerStates[truckName].index + 1
            );

        };


        viewer.showPrevious = function () {

            showImage(
                viewerStates[truckName].index - 1
            );

        };

    });


    /* =====================================================
       MANUAL ROTATION
       ===================================================== */

    document.querySelectorAll(".rotate-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const truckName =
                button.dataset.truck;

            const direction =
                button.dataset.direction;

            const viewer =
                document.querySelector(
                    `.truck-viewer[data-truck="${truckName}"]`
                );

            if (!viewer) {
                return;
            }

            if (direction === "left") {

                viewer.showPrevious();

            } else {

                viewer.showNext();

            }

        });

    });


    /* =====================================================
       AUTO ROTATION
       ===================================================== */

    document.querySelectorAll(".auto-rotate-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const truckName =
                button.dataset.truck;

            const viewer =
                document.querySelector(
                    `.truck-viewer[data-truck="${truckName}"]`
                );

            if (!viewer) {
                return;
            }

            const state =
                viewerStates[truckName];

            if (!state) {
                return;
            }


            if (state.timer) {

                clearInterval(state.timer);

                state.timer = null;

                button.classList.remove("running");

                button.innerHTML =
                    "▶ Auto Rotate";

            } else {

                state.timer = setInterval(function () {

                    viewer.showNext();

                }, 1800);

                button.classList.add("running");

                button.innerHTML =
                    "⏸ Stop Rotation";

            }

        });

    });

});