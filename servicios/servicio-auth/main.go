package main

import (
    "log"
    "os"
    "github.com/gin-gonic/gin"
    "github.com/joho/godotenv"
    "github.com/tuusuario/servicio-auth/handlers"
    "github.com/tuusuario/servicio-auth/middleware"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Println("No se encontró archivo .env")
    }

    port := os.Getenv("PORT")
    if port == "" {
        port = "8082"
    }

    router := gin.Default()
    router.GET("/health", handlers.Health)
    router.POST("/auth/login", handlers.Login)

    protected := router.Group("/auth")
    protected.Use(middleware.AuthMiddleware())
    {
        protected.GET("/validate", handlers.Validate)
    }

    log.Printf("Servicio Auth corriendo en :%s", port)
    router.Run(":" + port)
}
