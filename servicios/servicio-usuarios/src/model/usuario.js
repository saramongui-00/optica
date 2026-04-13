class Usuario {
  constructor(id, nombre, user, celular, email, password, estado, rol) {
    this.id = id;
    this.nombre = nombre;
    this.user = user;
    this.celular = celular;
    this.email = email;
    this.password = password;
    this.estado = estado || 'HABILITADO';
    this.rol = rol || 'SECRETARIO';
  }
}

module.exports = Usuario;