
function togglePassword() {
    const eyeIcon = document.querySelector('.eye-icon');
    const passwordInput = document.getElementById('password');
    if (passwordInput.type == "password") {
        passwordInput.type = "text";
        eyeIcon.src = "static/img/visible.png";
    } else {
        passwordInput.type = "password";
        eyeIcon.src = "static/img/hide.png";
    }
}

function copyTextPassword(idPassword) {
    let copyText = document.getElementById(idPassword);
    copyText.select();
    copyText.setSelectionRange(0, 30);
    navigator.clipboard.writeText(copyText.value)
    window.getSelection().removeAllRanges();
}

function openPopup(passwordId, currentAssociation) {
    document.getElementById("password-id-field").value = passwordId;

    header = document.querySelector('header');
    const scrollBarWidth = window.innerWidth - header.offsetWidth;
    document.body.classList.add('lock')
    document.body.style.paddingRight = scrollBarWidth + 'px';
    header.style.paddingRight = scrollBarWidth + 'px';

    const popup = document.getElementById('popup');
    popup.classList.add('active');
    popup.addEventListener('click', (e) => {
        if (!e.target.closest('.popup__content')) {
            closePopup();
        }
    })
}

function closePopup() {
    document.querySelector(".popup").classList.remove("active");

    setTimeout(() => {
        document.body.classList.remove('lock');
        document.body.style.paddingRight = '';
        document.querySelector('header').style.paddingRight = '';
        document.getElementById('association-field').value = '';
        document.getElementById('confirm-error').style.display = 'none';
    }, 300);
}

function validateForm(form) {
    form.addEventListener("submit", function(e) {

        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        const err = document.querySelector(".registration-login-form-error");
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const passwordPattern = /^[A-Za-z0-9!@#$%^&*()\-_+=.,<>/?\[\]{}\\|`~]+$/;

        if (email.length < 4) {
            e.preventDefault();
            err.textContent = "Мінімальна довжина пошти - 4 символи !";
        }  else if (password.length < 4) {
            e.preventDefault();
            err.textContent = "Мінімальна довжина паролю - 4 символи !";
        } else if (email.length > 50) {
            e.preventDefault();
            err.textContent = "Максимальна довжина пошти - 50 символів !";
        }  else if (password.length > 50) {
            e.preventDefault();
            err.textContent = "Максимальна довжина паролю - 50 символів !";
        } else if (!emailPattern.test(email)) {
            e.preventDefault();
            err.textContent = "Невірний формат пошти !";
        } else if (!passwordPattern.test(password)) {
            e.preventDefault();
            err.textContent = "Пароль може складатись тільки з латинських малих та великих літер, цифр та символів !@#$%^&*()-_=+.,<>/?[]{}\\|~";
        }
    });
}

function floatUpLine(form) {
    const inputs = form.querySelectorAll('input');
    inputs.forEach(input => {

        input.addEventListener('keydown', (e) => {
            if (e.key === ' ') {
                e.preventDefault();
            }
        });

        const placeholderText = input.getAttribute('placeholder') || '';
        input.removeAttribute('placeholder');

        const floatLabel = document.createElement('div');
        floatLabel.className = 'floating-placeholder';
        floatLabel.textContent = placeholderText;

        const wrapper = document.createElement('div');
        wrapper.className = 'form-group';
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);
        wrapper.appendChild(floatLabel);

        input.addEventListener('focus', () => {
            floatLabel.classList.add('active-placeholder');
        });

        input.addEventListener('blur', () => {
            if (input.value.length == 0) {
                floatLabel.classList.remove('active-placeholder');
            }
        });

        if (input.value.length !== 0) {
            floatLabel.classList.add('active-placeholder');
        }
    });
}

const rForm = document.getElementById("r-form");
const lForm = document.getElementById("l-form");
const forms = [lForm, rForm];

window.addEventListener("load", () => {
    forms.forEach(form => {
        if (form !== null) {
            validateForm(form);
            floatUpLine(form);
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        document.body.classList.add('transitions-enabled');
    }, 100);
});

const gForm = document.getElementById('g-form');
if (gForm !== null) {
    document.querySelectorAll('.checkbox').forEach(checkbox => {
        const input = checkbox.querySelector('input[type="checkbox"]');
        if (input.checked) {
            checkbox.classList.add('active');
        }
        checkbox.addEventListener('click', () => {
            if (checkbox.classList.contains('active')) {
                input.checked = false;
            } else {
                input.checked = true;
            }
            checkbox.classList.toggle('active');
        });
    })

    const rangeInput = document.querySelector('.length-range');
    let rangeValue = document.getElementById('range-value');
    rangeValue.innerText = `${rangeInput.value}`;
    rangeInput.addEventListener('input', () => {
        rangeValue.innerText = `${rangeInput.value}`;
    });
}

function setScrollToSession() {
    sessionStorage.setItem('scrollPos', window.scrollY);
}

const updateForm = document.querySelector('.popup__content');
if (updateForm) {
    const scrollPos = sessionStorage.getItem('scrollPos');
    if (scrollPos) {
        window.scrollTo(0, parseInt(scrollPos));
        sessionStorage.removeItem('scrollPos');
    }
    userInput = document.getElementById('association-field');
    confirmError = document.getElementById('confirm-error');
    updateForm.addEventListener('submit', (e) => {
        if (userInput.value.length == 0) {
            confirmError.style.display = 'block';
            confirmError.innerText = "Ви нічого не ввели !";
            e.preventDefault();
        } else if (userInput.value.length > 100) {
            confirmError.style.display = 'block';
            confirmError.innerText = "Довжина опису має НЕ перевищувати 100 символів !";
            e.preventDefault();
        }
    });
}




