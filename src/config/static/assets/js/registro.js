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
    category = document.getElementById('category').value;
    fechaInput = document.getElementById('fechaInput').value;
    horaSelect = document.getElementById('horaSelect').value;
    message = document.getElementById('message').value;
  
    axios.post('/fronted/Guardar_Clientes', {
      fullname: nombre.value,
      fullcorreo: correo.value,
      fullphone: phone.value,
    })
      .then(response => {
        const clienteId = response.data.id; // Extract the clienteId from the response
        console.log('Cliente guardado con ID:', clienteId);
        // Save the appointment data using the clienteId
        axios.post('/Guardar_Citas', {
          data:{
          clienteId: clienteId,
          fullcategory: category,
          fullfechaInput: fechaInput,
          fullhoraSelect: horaSelect,
          fullmessage: message,
          }
        })
          .then(response => {
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