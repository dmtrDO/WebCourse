
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




