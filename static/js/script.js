//sidebar start
function openNav() {
    'use strict';
    const sidepanel = document.getElementById('mySidepanel')
    if (sidepanel) {
        sidepanel.style.left = '0';
    }
    else {
        console.error('error: side panel not found');
    }
}
function closeNav() {
    'use strict';
    const sidepanel = document.getElementById('mySidepanel');
    if (sidepanel) {
        sidepanel.style.left = '-320px';
    }
    else {
        console.error('error: side panel not found');
    }
}
function open_search() {
    'use strict';
    const searchpanel = document.getElementById('search-bar');
    if (searchpanel) {
        searchpanel.style.height = '100vh';
        searchpanel.style.borderRadius = '0';
    }
    else {
        console.error('error: side panel not found');
    }
}
function close_search() {
    'use strict';
    const searchpanel = document.getElementById('search-bar');
    if (searchpanel) {
        searchpanel.style.height = '0';
        searchpanel.style.borderTopLeftRadius = '100%';
        searchpanel.style.borderTopRightRadius = '100%';
    }

    else {
        console.error('error: side panel not found');
    }
}
//right sidebar {
function open_right_side() {
    'use strict';
    const rightside = document.getElementById('right_side');
    if (rightside) {
        rightside.style.right = '0';
    }
    else {
        console.error('error: right panel not found');
    }
}
function close_right_side() {
    'use strict';
    const rightside = document.getElementById('right_side');
    if (rightside) {
        rightside.style.right = '-355px';
    }
    else {
        console.error('error: right panel not found');
    }
}
//portfolio gallary
function open_img(evt, cityName) {
    let i, tabcontent, tablinks;
    //hide all tab content
    tabcontent = document.getElementsByClassName('tabcontent');
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    //remove active class from all tab links
    tablinks = document.getElementsByClassName('tablinks');
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    //show the selected tab content and mark the corresponding tab link
    //as active
    document.getElementById(cityName).style.display = 'block';
    evt.currentTarget.classList.add('active');
}
// faq section
document.addEventListener('DOMContentLoaded', function () {
    let accordionButtons = document.querySelectorAll('.accordion-button');
    let acoimg = document.querySelectorAll('.accordion-button img');
    accordionButtons.forEach(function (button, index) {
        button.addEventListener('click', function () {
            let collapse = this.parentElement.nextElementSibling;
            // Close All the Other Accordion Items
            accordionButtons.forEach(function (otherButton, otherIndex) {
                if (otherButton !== button) {
                    let otherCollapse = otherButton.parentElement.nextElementSibling;
                    otherCollapse.style.maxHeight = null;
                    // Reset the Image Source and Rotation for Other Accordion Items
                    acoimg[otherIndex].src = '/static/images/icon/plus.png';
                    acoimg[otherIndex].style.transform = 'rotate(0deg,)';
                    otherButton.style.backgroundColor = "#fff"
                }
            });
            // Toggle the Clicked According Item
            if (collapse.style.maxHeight) {
                collapse.style.maxHeight = null;
                // Reset the Image Source, Rotation, and Background Color When Collapsing
                acoimg[index].src = '/static/images/icon/plus.png';
                acoimg[index].style.transform = 'rotate(90deg)'
                button.style.backgroundColor = '';
            }
            else {
                collapse.style.maxHeight = collapse.scrollHeight + 'px';

                // Change the Image Source, Set Rotation, and Background Color When Expanding
                acoimg[index].src = '/static/images/icon/menus.png';
                acoimg[index].style.transform = 'rotate(180deg)'
                button.style.backgroundColor = '#c1b0b5'
            }
        });
    });
});
// Footer Validation Start
const fom = document.getElementById('footer-form');
const footerMessage = document.getElementById('footer-message');
fom.addEventListener('submit', (event) => {
    event.preventDefault();
    footerMessage.innerHTML = '~form submitted success fully';
    footerMessage.style.display = 'flex';
    fom.reset();
    setTimeout(() => {
        footerMessage.style.display = 'none'
    }, 3000);
});
// Button Back ti Top
window.onscroll = function () {
    scrollFunction()
};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('backToTopBtn').style.display = 'block';
    }
    else {
        document.getElementById('backToTopBtn').style.display = 'none';
    }
};
function scrollToTop() {
    const scrollToTopBtn = document.documentElement || document.body;
    scrollToTopBtn.scrollIntoView({
        behavior: 'smooth'
    });
};
//responsive logoipsum
$('.sliderlogo').slick({
    arrows: false,
    dots: false,
    Infinity: false,
    autoplay: false,
    speed: 300,
    slidesToShow: 5,
    sliderToScroll: 1,
    responsive: [{
        breakpoint: 1024,
        settings: {
            slidesToShow: 4,
            sliderToScroll: 1,
            Infinity: true,
            dots: false
        }
    },
    {
        breakpoint: 600,
        settings: {
            slidesToShow: 2,
            sliderToScroll: 1
        }
    },
    ]
});