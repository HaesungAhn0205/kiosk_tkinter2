import tkinter as tk


class KioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kiosk 프로그램")
        self.root.state('zoomed')  # 창 크기를 최대화하는 설정

        # 상품 목록 및 가격 정보
        self.products = {"상품A": 1000, "상품B": 1000, "상품C": 1000, "상품D": 1000, "상품E": 1000,
                         "상품F": 1000, "상품G": 1000, "상품H": 1000, "상품I": 1000, "상품J": 1000}

        # 메뉴 수량과 장바구니 초기화
        self.menu_quantities = {product: tk.IntVar() for product in self.products}
        self.shopping_cart = {product: tk.IntVar() for product in self.products}

        # 환영 메시지
        self.label = tk.Label(root, text="상품을 선택하세요:")
        self.label.pack(pady=10)

        # 상품 버튼 및 가격 정보 추가
        for product, price in self.products.items():
            button_frame = tk.Frame(root)
            button_frame.pack(side=tk.LEFT, padx=5, pady=5)

            button = tk.Button(button_frame, text=product, width=10, height=2,
                               command=lambda p=product: self.add_to_cart(p))
            button.pack()

            price_label = tk.Label(button_frame, text=f"{price}원", font=("Arial", 8), fg="gray")
            price_label.pack()

        # 결제 버튼
        self.confirm_button = tk.Button(root, text="결제", command=self.display_cart)
        self.confirm_button.pack(pady=10)

        # 장바구니 내용 표시
        self.cart_label = tk.Label(root, text="")
        self.cart_label.pack(pady=10)

    def add_to_cart(self, product):
        # 메뉴 수량 증가
        self.menu_quantities[product].set(self.menu_quantities[product].get() + 1)

        # 장바구니에 메뉴 추가
        for product in self.products:
            quantity = self.menu_quantities[product].get()
            self.shopping_cart[product].set(quantity)

        # 장바구니 내용 업데이트
        result_message = "장바구니 내용:\n"
        for product, quantity in self.shopping_cart.items():
            if quantity.get() > 0:
                result_message += f"{product}: {quantity.get()}개\n"

        self.cart_label.config(text=result_message)

    def display_cart(self):
        # 결제 버튼 클릭 시 처리 (여기서는 장바구니 내용만 출력)
        result_message = "장바구니 내용:\n"
        for product, quantity in self.shopping_cart.items():
            if quantity.get() > 0:
                result_message += f"{product}: {quantity.get()}개\n"

        self.label.config(text=result_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop()
