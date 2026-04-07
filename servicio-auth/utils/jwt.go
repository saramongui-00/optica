package utils

import (
    "os"
    "time"
    "github.com/golang-jwt/jwt/v5"
)

type Claims struct {
    UserID string `json:"user_id"`
    Email  string `json:"email"`
    Role   string `json:"role"`
    jwt.RegisteredClaims
}

func GenerateJWT(userID, email, role string) (string, error) {
    secret := []byte(os.Getenv("JWT_SECRET"))
    expiration := time.Now().Add(time.Hour * 24)

    claims := Claims{
        UserID: userID,
        Email:  email,
        Role:   role,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(expiration),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
        },
    }

    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(secret)
}

func ValidateJWT(tokenString string) (*Claims, error) {
    secret := []byte(os.Getenv("JWT_SECRET"))
    claims := &Claims{}

    token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
        return secret, nil
    })

    if err != nil || !token.Valid {
        return nil, err
    }

    return claims, nil
}
