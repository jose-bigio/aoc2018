package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

/*
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
*/

type claim struct {
	id        int
	leftStart int
	topStart  int
	width     int
	height    int
}

// newClaim creates a claim from parsing an entry string (ie. #1 @ 1,3: 4x4)
func newClaim(entry string) (*claim, error) {
	splitEntry := strings.Split(entry, " ")
	// After this if string started as #1 @ 1,3: 4x4
	// splitEntry[0] = #1
	// splitEntry[1] = @
	// splitEntry[2] = 1,3:
	// splitEntry[3] = 4x4

	c := claim{}
	id, err := strconv.Atoi(splitEntry[0][1:])
	if err != nil {
		return nil, err
	}
	c.id = id

	commaIndex := strings.Index(splitEntry[2], ",")
	leftStart, err := strconv.Atoi(splitEntry[2][:commaIndex])
	if err != nil {
		return nil, err
	}
	c.leftStart = leftStart

	topStart, err := strconv.Atoi(splitEntry[2][commaIndex+1 : len(splitEntry[2])-1])
	if err != nil {
		return nil, err
	}
	c.topStart = topStart

	xIndex := strings.Index(splitEntry[3], "x")
	width, err := strconv.Atoi(splitEntry[3][:xIndex])
	if err != nil {
		return nil, err
	}
	c.width = width

	height, err := strconv.Atoi(splitEntry[3][xIndex+1:])
	if err != nil {
		return nil, err
	}
	c.height = height
	return &c, nil
}

func (c *claim) updateGrid(inputGrid map[int]map[int][]int, count *int, noOverlaps map[int]struct{}) {
	hasOverlap := false
	for x := c.leftStart; x < c.leftStart+c.width; x++ {
		if _, exists := inputGrid[x]; !exists {
			inputGrid[x] = make(map[int][]int)
		}
		for y := c.topStart; y < c.topStart+c.height; y++ {
			if _, exists := inputGrid[x][y]; !exists {
				inputGrid[x][y] = make([]int, 1)
				inputGrid[x][y][0] = c.id
			} else {
				// map already exists, so it's a duplicate entry
				hasOverlap = true

				// We will mark it as true after we say this square has already been claimed more than once
				if len(inputGrid[x][y]) == 1 {
					*count++
				}
				// At this point, we need to remove the overlapped ones from the map
				for _, i := range inputGrid[x][y] {
					delete(noOverlaps, i)
				}

				inputGrid[x][y] = append(inputGrid[x][y], c.id)
			}
		}
	}
	if !hasOverlap {
		noOverlaps[c.id] = struct{}{}
	}
}

func main() {
	inputFile, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer inputFile.Close()

	inputGrid := make(map[int]map[int][]int)
	count := 0
	noOverlaps := make(map[int]struct{})

	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		c, err := newClaim(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		c.updateGrid(inputGrid, &count, noOverlaps)
	}
	fmt.Println(count)
	fmt.Println(noOverlaps)
}
