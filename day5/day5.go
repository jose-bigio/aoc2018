package main

// Corey please fix this

import (
	"container/list"
	"encoding/binary"
	"fmt"
	"io/ioutil"
	"math"
)

func readInput(fileName string) (*list.List, error) {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}
	elements := list.New()
	for _, char := range data {
		elements.PushBack(byte(char))
	}

	return elements, nil
}

func interfaceToFloat(v interface{}) float64 {
	byteValue, _ := (v).(*[]byte)
	fmt.Printf("Inputting %v\n", *byteValue)
	bits := binary.LittleEndian.Uint64(*byteValue)
	return math.Float64frombits(bits)
}

func updateList(list *list.List) bool {
	previous := list.Front()
	current := previous.Next()
	for ; current != nil; current = current.Next() {
		if math.Abs((interfaceToFloat(previous.Value) - interfaceToFloat(current.Value))) == 32 {
			return true
		}
		previous = current
	}

	return false
}

func main() {
	elements, err := readInput("input.txt")
	if err != nil {
		panic(err)
	}
	for updateList(elements) {
	}
	fmt.Printf("Length is %d", elements.Len())

}
