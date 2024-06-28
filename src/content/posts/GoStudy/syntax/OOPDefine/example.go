package main

import (
	"fmt"
	"math"
	"reflect"
)

type IShape interface {
	PrintName() string
	GetArea() float64
}

type Shape struct {
	name string
}

func (s *Shape) PrintName() string {
	return "this shape hasn't name"
}

func (s *Shape) GetArea() float64 {
	return -1
}

type Circle struct {
	Shape
	radius float64
}

func (c *Circle) PrintName() string {
	return "Circle"
}
func (c *Circle) GetArea() float64 {
	return math.Pi * c.radius * c.radius
}

func main() {
	var circle Circle = Circle{}

	fmt.Println(reflect.TypeOf(circle))

	circle.radius = 10

	var a IShape = &circle

	fmt.Println(reflect.TypeOf(a))

	fmt.Println(a.PrintName())

}
