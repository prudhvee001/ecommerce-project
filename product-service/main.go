package main

import (
	"encoding/json"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

type Product struct {
	ID    int     `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

func main() {
	r := gin.Default()

	r.GET("/products", func(c *gin.Context) {
		data, err := ioutil.ReadFile("products.json")
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "File read failed"})
			return
		}

		var products []Product
		if err := json.Unmarshal(data, &products); err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "JSON parse failed"})
			return
		}

		c.JSON(http.StatusOK, products)
	})

	r.Run(":3002") // Service will run on port 3002
}
