// dot.cpp
#include <ctime>
#include <cstdlib>
#include <chrono>
#include <iostream>

class Matrix {
    float *data;
public:
    size_t n, m;
    Matrix(size_t r, size_t c): data(new float[r*c]), n(r), m(c) {}
    ~Matrix() { delete[] data; }
    float& operator() (size_t x, size_t y) { return data[x*m+y]; }
    float operator() (size_t x, size_t y) const { return data[x*m+y]; }
};

float dot(const Matrix &a, const Matrix& b) {
    Matrix c(a.n, b.m);
    for (size_t i = 0; i < a.n; ++i)
        for (size_t j = 0; j < b.m; ++j) {
            float s = 0;
            for (size_t k = 0; k < a.m; ++k)
                s += a(i, k) * b(k, j);
            c(i, j) = s;
        }
    return c(0, 0); // to comfort -O2 optimization
}

void fill_rand(Matrix &a) {
    for (size_t i = 0; i < a.n; ++i)
        for (size_t j = 0; j < a.m; ++j)
            a(i, j) = rand() / static_cast<float>(RAND_MAX) * 2 - 1;
}

int main() {
    srand((unsigned)time(NULL));
    const int n = 100, p = 200, m = 50, T = 100;
    Matrix a(n, p), b(p, m);
    fill_rand(a);
    fill_rand(b);
    auto st = std::chrono::system_clock::now();
    float s = 0;
    for (int i = 0; i < T; ++i) {
        s += dot(a, b);
    }
    auto ed = std::chrono::system_clock::now();
    std::chrono::duration<double> diff = ed-st;
    std::cerr << s << std::endl;
    std::cout << T << " loops. average " << diff.count() * 1e6 / T << "us" << std::endl;
}