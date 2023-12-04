// function guardar() {
//     nombre = document.getElementById('name')
//     correo = document.getElementById('email_address')
//     phone = document.getElementById('phone')

//     axios.post('/fronted/Guardar_Clientes',{
//       fullname: nombre.value,
//       fullcorreo: correo.value,
//       fullphone: phone.value,
//     })
//   .then( response => {
//       console.log(response.data);
//       console.log('datos guardados exitosamente')
//   }).catch(function (error) {
//       console.log(error);
//  })
//  }
function guardar() {
    nombre = document.getElementById('name');
    correo = document.getElementById('email_address');
    phone = document.getElementById('phone');
  
    axios.post('/fronted/Guardar_Clientes', {
      fullname: nombre.value,
      fullcorreo: correo.value,
      fullphone: phone.value,
    })
      .then(response => {
        const clienteId = response.data.id; // Extract the clienteId from the response
        console.log('Cliente guardado con ID:', clienteId);
  
        // Save the appointment data using the clienteId
        category = document.getElementById('category');
        fechaInput = document.getElementById('fechaInput');
        horaSelect = document.getElementById('horaSelect');
        message = document.getElementById('message');
  
        axios.post('/Guardar_Citas', {
          data:{
          clienteId: response.data.id,
          fullcategory: category.value,
          fullfechaInput: fechaInput.value,
          fullhoraSelect: horaSelect.value,
          fullmessage: message.value,
          }
        })
          .then(response => {
            alert(data['category'])
            console.log('Cita guardada para el cliente con ID:', clienteId);
            console.log('datos cita guardados exitosamente');
          })
          .catch(function (error) {
            console.log(error);
          });
      })
      .catch(function (error) {
        console.log(error);
      });
  }


  
  
//   function cita() {
//   }