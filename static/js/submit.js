var submitForm = function() {
    var name = document.getElementById('fullname').value;
    var address = document.getElementById('address').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost:5000/api/Access', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
            name: name,
            address: address,
            email: email,
            phone: phone
    }));
    location.reload();
}