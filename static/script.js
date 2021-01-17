
function aboutProject(message){
    const check = document.getElementById('check')
    document.getElementById('text').innerHTML = '<h5 id="check">' + message + '</h5>'

    if (check != null) {
        document.getElementById('text').innerHTML = ''
    }
};

