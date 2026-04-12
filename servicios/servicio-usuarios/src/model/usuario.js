class Usuario {
  constructor(id, nombre, user, celular, email, password, estado) {
    this.id = id;
    this.nombre = nombre;
    this.user = user;
    this.celular = celular;
    this.email = email;
    this.password = password;
    this.estado = estado || 'HABILITADO';
  }
}

module.exports = Usuario;