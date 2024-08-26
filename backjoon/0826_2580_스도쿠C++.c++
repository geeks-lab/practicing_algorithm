#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> array(9, vector<int>(9));
int zeroCnt = 0;

// 특정 숫자가 해당 위치에 놓일 수 있는지 확인하는 함수
bool is_valid(int x, int y, int num) {
    for (int i = 0; i < 9; ++i) {
        if (array[x][i] == num || array[i][y] == num) {
            return false;
        }
    }
    int start_x = 3 * (x / 3), start_y = 3 * (y / 3);
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (array[start_x + i][start_y + j] == num) {
                return false;
            }
        }
    }
    return true;
}

// 백트래킹을 이용한 스도쿠 해결 함수
bool solve_sudoku() {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (array[i][j] == 0) {
                for (int num = 1; num <= 9; ++num) {
                    if (is_valid(i, j, num)) {
                        array[i][j] = num;
                        zeroCnt--;
                        if (solve_sudoku()) {
                            return true;
                        }
                        array[i][j] = 0;
                        zeroCnt++;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cin >> array[i][j];
            if (array[i][j] == 0) {
                zeroCnt++;
            }
        }
    }

    solve_sudoku();

    for (const auto &row : array) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
