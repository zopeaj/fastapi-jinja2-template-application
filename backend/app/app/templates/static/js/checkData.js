var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "name": "Item Datas",
  "age": 23,
  "business": "Ecommerce-App"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
};

fetch("http://127.0.0.1:8000/main/items/create/item/", requestOptions)
  .then(response => response.json())
  .then(result => {
       console.log(result)
       alert(JSON.stringify(result, null, 2))
     }
   )
  .catch(error => console.log('error', error));

// function checkStatus(response) {
//     const checkStatus = response => {
//       if(response.ok) {
//         return response;
//       }
//       const error = new Error(response.statusText);
//       error.response = response;
//       return Promise.reject(error);
//     }
//   }

// contents = {
//   "name": "Item Datas",
//   "age": 23,
//   "business": "Ecommerce-App"
// }


// var request = fetch("http://127.0.0.1:8000/main/items/create/item/",{
// method: "POST",
// headers: {"Content-Type": "application/json"},
// body: JSON.stringify(contents)
// }).then(checkStatus)

// request
//        .then(res => res.text())
//        .then(data => {
//           console.log(data)
//       }).catch(err => console.log(err));


