// class RequestData {
//   constructor(data){
//     this.data = data
//     this.setData = null;
//   }

//   getData() {
//     return this.data;
//   }

//   setDataResponse(data) {
//     this.setData = data;
//   }

//   getDataResponse() {
//     return this.setData;
//   }

//   checkStatus(response) {
//     const checkStatus = response => {
//       if(response.ok) {
//         return response;
//       }
//       const error = new Error(response.statusText);
//       error.response = response;
//       return Promise.reject(error);
//     }
//   }

//   fetcData() {
//     var request = fetch("http://127.0.0.1:8000/main/items/create/item/",{
//     method: "POST",
//     headers: {"Content-Type": "application/json"},
//     body: JSON.stringify(this.getData())
//     }).then(this.checkStatus);
//     return request;
//   }
// }


contents = {
  "name": "Item Datas",
  "age": 23,
  "business": "Ecommerce-App"
}

// var requestData = new RequestData(contents)
// var responseData = requestData.fetcData();
// responseData.then(res => res.json()).then(data => requestData.setDataResponse(data)).catch(err => console.log(err)).finally(console.log("Hello"))


function checkStatus(response) {
    const checkStatus = response => {
      if(response.ok) {
        return response;
      }
      const error = new Error(response.statusText);
      error.response = response;
      return Promise.reject(error);
    }
  }

function createItemData() {
  var request = fetch("http://127.0.0.1:8000/main/items/create/item/",{
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify(contents)
  }).then(this.checkStatus);

  request.then(res => {
      res.json()
  }).then(data => {
    alert(JSON.stringify(data, null, 2));
    return data
  }).catch(err => {
    console.log(err);
  }).finally(console.log("Hello"));
}

createItemData()


