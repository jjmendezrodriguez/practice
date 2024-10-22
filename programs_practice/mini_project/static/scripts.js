document.addEventListener('DOMContentLoaded', function () {
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');
    const loginModal = document.getElementById('login-modal');
    const closeButton = document.getElementById('close-button');
    const loginForm = document.getElementById('login-form');
    const registerLink = document.getElementById('register-link');
    const forgotPasswordLink = document.getElementById('forgot-password-link');
    const create_user = document.getElementById('create_user');

    // Muestra el modal de login cuando se hace clic en el enlace de login
    loginLink.addEventListener('click', function (event) {
        event.preventDefault();
        loginModal.style.display = 'block';
    });

    // Cierra el modal de login cuando se hace clic en el botón de cerrar
    closeButton.addEventListener('click', function () {
        loginModal.style.display = 'none';
    });

    // Cierra el modal de login cuando se hace clic fuera del modal
    window.addEventListener('click', function (event) {
        if (event.target == loginModal) {
            loginModal.style.display = 'none';
        }
    });

    // Maneja el evento de envío del formulario de login
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Aquí puedes agregar tu lógica de autenticación
        if (username === 'user' && password === 'password') {
            alert('Login successful');
            loginModal.style.display = 'none';
            loginLink.style.display = 'none';
            logoutLink.style.display = 'block';
        } else {
            alert('Invalid credentials');
        }
    });

    // Maneja el evento de clic en el enlace de logout
    logoutLink.addEventListener('click', function (event) {
        event.preventDefault();
        loginLink.style.display = 'block';
        logoutLink.style.display = 'none';
    });

    // Maneja los nuevos usuarios
    registerLink.addEventListener('click', function (event) {
        event.preventDefault();
        window.location.href = '/register';
    });

    create_user.addEventListener('click', function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        document.getElementById('message_1').innerText = '';
        document.getElementById('message_2').innerText = '';
        document.getElementById('message_3').innerText = '';

        if (password !== confirmPassword) {
            document.getElementById('message_1').innerText = "Passwords do not match, Please try again.";
            return;
        }

        fetch('http://localhost:5000/register_user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.error) {
                document.getElementById('message_2').innerText = data.error;
            } else {
                document.getElementById('message_3').innerText = "User registered successfully!\nWelcome!";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('message_2').innerText = "An error occurred. Please fill all the blanks.";
        });
    })
    
    // Maneja cuando se te olvida el password
    forgotPasswordLink.addEventListener('click', function (event) {
        event.preventDefault();
        alert('Redirect to forgot password page or show forgot password modal');
    });
});
