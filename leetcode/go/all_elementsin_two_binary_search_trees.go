package main

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	allElements := getElements(root1)
	allElements = append(allElements, getElements(root2)...)
	sort.Ints(allElements)
	return allElements
}

func getElements(root *TreeNode) []int {
	var elements []int
	seenElements := make(map[TreeNode]bool)
	elementsToProcess := []*TreeNode{root}
	for len(elementsToProcess) != 0 {
		elementsCount := len(elementsToProcess)
		element := elementsToProcess[elementsCount-1]
		elementsToProcess = elementsToProcess[:elementsCount-1]
		if element == nil {
			continue
		}

		if seenElements[*element] == true {
			elements = append(elements, element.Val)
		} else {
			seenElements[*element] = true
			elementsToProcess = append(elementsToProcess, element.Right, element, element.Left)
		}
	}
	return elements
}
