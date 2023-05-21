function validarFormulario(event) {

    event.preventDefault()
  
    let user = document.formRegistro.user.value
    let email = document.formRegistro.email.value
    let password = document.formRegistro.password.value
    let enter = true
    if (user.length < 8) {
      alert('ingrese un nombre de usuario válido, que sea mayor a 8 caracteres')
      document.formregistro.user.focus()
      enter = false
    }
  
    if (!email.includes('@') && !email.includes('.')) {
      alert('por favor, verifica tu email')
      document.formRegistro.email.focus()
      enter = false
    }
  
    if (password.length < 8) {
      alert('La contraseña debe ser mayor a 8 caracteres')
      document.formRegistro.password.focus()
      enter = false
    }
    
    if (enter === true) {
    window.location = '/login.html'
    } else {
      alert('Por favor, verifica los datos ingresados')
    }
  
  }
  
  function validarLogin(event) {
  
    event.preventDefault()
  
    let user = document.formLogin.user.value
    let password = document.formLogin.password.value
    let enter = true
  
    if (user.length < 8) {
      alert('ingrese un nombre de usuario válido, que sea mayor a 8 caracteres')
      document.formLogin.user.focus()
      enter = false
    }
  
    if (password.length < 8) {
      alert('La contraseña debe ser mayor a 8 caracteres')
      document.formLogin.password.focus()
      enter = false
    }
  
    if (!user.value === 'admin123' && !password.value === 'admin123'){
      alert('usuario o contraseña incorrectos')
      enter = false
    }
  
    if (enter === true) {
      window.location = '/index.html'
      } else {
        alert('Por favor, verifica los datos ingresados')
      }
    
  
  }
  