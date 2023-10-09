import sympy as sym

def main():
    x = sym.symbols('x')
    f = x**2 - 3*x + 2

    # Tính tích phân
    integral = sym.integrate(f, x)
    print("Tích phân của f(x):", integral)

    # Đạo hàm
    derivative = sym.diff(f, x)
    print("Đạo hàm của f(x):", derivative)

    # Giải phương trình
    equation = sym.Eq(x**2 + 3*x, 10)
    solutions = sym.solve(equation, x)
    print("Nghiệm của phương trình:", solutions)

    # Biểu đồ hàm số
    import sympy.plotting as syp
    syp.plot(f, (x, -5, 5), title='Đồ thị hàm số f(x)')

if __name__ == "__main__":
    main()
