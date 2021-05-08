public class Order {
    boolean isFilled;
    double billAmount;
    String shipping;

    public Order(boolean filled, double cost, String shippingMethod) {
        if (cost > 24.00) {
            System.out.println("High value item!");
        } else {
            System.out.println("Low value item!");
        }
        isFilled = filled;
        billAmount = cost;
        shipping = shippingMethod;
    }

    public void ship() {
        if (isFilled) {
            System.out.println("Shipping");
        } else System.out.println("Order not ready");

        double shippingCost = calculateShipping();

        System.out.println("Shipping cost: ");
        System.out.println(shippingCost);
    }

    public double calculateShipping() {
        switch (shipping) {
            case "Regular" -> {
                return 0;
            }
            case "Express" -> {
                return 1.75;
            }
            default -> {
                return .50;
            }
        }
    }

    public static void main(String[] args) {
        // create instances and call methods here!

    }
}

