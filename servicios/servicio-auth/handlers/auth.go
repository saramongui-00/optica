package handlers

import (
    "net/http"
    "github.com/gin-gonic/gin"
    "github.com/tuusuario/servicio-auth/utils"
)

var users = map[string]map[string]string{
    "cliente1@optica.com": {
        "id":       "1",
        "password": "cliente123",
        "role":     "client",
        "name":     "Juan Pérez",
    },
    "doctor@optica.com": {
        "id":       "2",
        "password": "doctor123",
        "role":     "optometrist",
        "name":     "Dra. Ana Gómez",
    },
}

type LoginRequest struct {
    Email    string `json:"email" binding:"required"`
    Password string `json:"password" binding:"required"`
}

func Login(c *gin.Context) {
    var req LoginRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Datos inválidos"})
        return
    }

    user, exists := users[req.Email]
    if !exists || user["password"] != req.Password {
        c.JSON(http.StatusUnauthorized, gin.H{"error": "Credenciales inválidas"})
        return
    }

    token, err := utils.GenerateJWT(user["id"], req.Email, user["role"])
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Error generando token"})
        return
    }

    c.JSON(http.StatusOK, gin.H{
        "token": token,
        "user": gin.H{
            "id":    user["id"],
            "email": req.Email,
            "role":  user["role"],
            "name":  user["name"],
        },
    })
}

func Validate(c *gin.Context) {
    authHeader := c.GetHeader("Authorization")
    if authHeader == "" {
        c.JSON(http.StatusUnauthorized, gin.H{"error": "Token requerido"})
        return
    }

    token := authHeader
    if len(token) > 7 && token[:7] == "Bearer " {
        token = token[7:]
    }

    claims, err := utils.ValidateJWT(token)
    if err != nil {
        c.JSON(http.StatusUnauthorized, gin.H{"error": "Token inválido"})
        return
    }

    c.JSON(http.StatusOK, gin.H{
        "valid":   true,
        "user_id": claims.UserID,
        "email":   claims.Email,
        "role":    claims.Role,
    })
}

func Health(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{"status": "Servicio Auth OK"})
}
