const API_URL = 'http://192.168.59.12:5000'; // app1 IP

function fetchVotes() {
  fetch(API_URL + '/')
    .then(response => response.json())
    .then(data => {
      document.getElementById('results').innerHTML = `
        <p>🐱 Cat: ${data.cat || 0}</p>
        <p>🐶 Dog: ${data.dog || 0}</p>
      `;
    });
}

function vote(option) {
  fetch(API_URL + '/vote?vote=' + option, {
    method: 'POST'
  }).then(() => {
    fetchVotes();
  });
}

fetchVotes();
