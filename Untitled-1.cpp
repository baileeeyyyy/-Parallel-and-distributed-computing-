//Question one DAA Assignment

#include <algorithm> // For std::swap function

// Function to sort an array using Selection Sort
void selectionSort(int arr[], int n) {
    // Loop through the entire array
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i; // Assume the current element is the smallest
        for (int j = i + 1; j < n; j++) {
            // If a smaller element is found, update the index
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        // Swap the smallest element with the current element
        std::swap(arr[minIdx], arr[i]);
    }
}

// Function to sort an array using Bubble Sort
void bubbleSort(int arr[], int n) {
    // Loop through the entire array
    for (int i = 0; i < n - 1; i++) {
        // Compare adjacent elements and swap if out of order
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1])
                std::swap(arr[j], arr[j + 1]);
        }
    }
}

// Function to sort an array using Insertion Sort
void insertionSort(int arr[], int n) {
    // Start from the second element
    for (int i = 1; i < n; i++) {
        int key = arr[i]; // Store the current element
        int j = i - 1;
        // Move elements that are greater than `key` one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        // Place the key in its correct position
        arr[j + 1] = key;
    }
}


//Generate Random Arrays
#include <cstdlib> // For random number generation
#include <ctime>   // For setting a random seed

// Function to generate a random array
void generateRandomArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000; // Generate random numbers between 0 and 9999
    }
}


//Measure Execution Times
#include <iostream>  // For input/output
#include <chrono>    // For measuring execution time

int main() {
    const int sizes[] = {10, 50, 100, 1000, 10000}; // Array sizes to test
    
    // Loop through each size
    for (int n : sizes) {
        int A1[n], A2[n], A3[n];
        generateRandomArray(A1, n); // Generate random array for Insertion Sort
        generateRandomArray(A2, n); // Generate random array for Selection Sort
        generateRandomArray(A3, n); // Generate random array for Bubble Sort

        // Measure Insertion Sort
        auto start = std::chrono::high_resolution_clock::now(); // Start the timer
        insertionSort(A1, n); // Sort the array using Insertion Sort
        auto end = std::chrono::high_resolution_clock::now(); // Stop the timer
        auto durationInsertion = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count(); // Calculate time taken

        // Measure Selection Sort
        start = std::chrono::high_resolution_clock::now(); // Start the timer
        selectionSort(A2, n); // Sort the array using Selection Sort
        end = std::chrono::high_resolution_clock::now(); // Stop the timer
        auto durationSelection = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count(); // Calculate time taken

        // Measure Bubble Sort
        start = std::chrono::high_resolution_clock::now(); // Start the timer
        bubbleSort(A3, n); // Sort the array using Bubble Sort
        end = std::chrono::high_resolution_clock::now(); // Stop the timer
        auto durationBubble = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count(); // Calculate time taken

        // Display Results
        std::cout << "N = " << n << "\n";
        std::cout << "Insertion Sort: " << durationInsertion << " µs\n";
        std::cout << "Selection Sort: " << durationSelection << " µs\n";
        std::cout << "Bubble Sort: " << durationBubble << " µs\n\n";
    }

    return 0;
}
