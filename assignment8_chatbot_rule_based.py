PRODUCTS = {
    "iphone 15": [59999, 4.5, 12500, "In Stock"],
    "samsung galaxy s24": [74999, 4.4, 9800, "In Stock"],
    "oneplus 12": [64999, 4.6, 7600, "In Stock"],
}


def chatbot():
    print("Available products:", ", ".join(PRODUCTS))
    product = input("Enter a product name: ").strip().lower()
    if product not in PRODUCTS:
        print("Product not found!")
        return

    price, rating, reviews, availability = PRODUCTS[product]
    print("Ask about price, rating, reviews, availability, or a recommendation.")

    while True:
        question = input("You: ").strip().lower()
        if question == "bye":
            print("Goodbye!")
            break
        elif "price" in question or "cost" in question:
            print("Price: ₹", price)
        elif "rating" in question:
            print("Rating:", rating, "/5")
        elif "review" in question:
            print("Reviews:", reviews)
        elif "availability" in question or "stock" in question:
            print("Availability:", availability)
        elif "recommend" in question or "buy" in question:
            print("Recommended!" if rating >= 4.5 else "Compare before buying.")
        else:
            print("Sorry, query not understood.")


def main():
    chatbot()


if __name__ == "__main__":
    main()