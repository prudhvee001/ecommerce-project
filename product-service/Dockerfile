FROM golang:1.21
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o product-service
EXPOSE 3002
CMD ["./product-service"]
