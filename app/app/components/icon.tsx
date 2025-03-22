import {
  Badge,
  PiggyBank,
  Book,
  Shirt,
  Dumbbell,
  Smartphone,
  Home,
  Plane,
  Coffee,
  Crown,
  ShoppingCart,
  UtensilsCrossed,
  Heart,
  ShoppingBag,
  Car,
  Gamepad2,
  Gift,
  DollarSign,
  CreditCard,
  Wallet,
  Tag,
} from "lucide-react";

export const iconList = [
  "shopping-cart",
  "utensils-crossed",
  "heart",
  "shopping-bag",
  "car",
  "gamepad2",
  "gift",
  "crown",
  "coffee",
  "plane",
  "home",
  "dumbbell",
  "shirt",
  "piggy-bank",
  "dollar-sign",
  "credit-card",
  "wallet",
  "other",
  "book",
  "smartphone",
] as const;

export type IconName = (typeof iconList)[number];

interface IconProps {
  icon: IconName;
}
export const Icon = ({ icon }: IconProps) => {
  const iconSize = 36;

  switch (icon) {
    case "shopping-cart":
      return <ShoppingCart size={iconSize} />;
    case "utensils-crossed":
      return <UtensilsCrossed size={iconSize} />;
    case "heart":
      return <Heart size={iconSize} />;
    case "shopping-bag":
      return <ShoppingBag size={iconSize} />;
    case "car":
      return <Car size={iconSize} />;
    case "gamepad2":
      return <Gamepad2 size={iconSize} />;
    case "gift":
      return <Gift size={iconSize} />;
    case "crown":
      return <Crown size={iconSize} />;
    case "coffee":
      return <Coffee size={iconSize} />;
    case "plane":
      return <Plane size={iconSize} />;
    case "home":
      return <Home size={iconSize} />;
    case "dumbbell":
      return <Dumbbell size={iconSize} />;
    case "shirt":
      return <Shirt size={iconSize} />;
    case "piggy-bank":
      return <PiggyBank size={iconSize} />;
    case "dollar-sign":
      return <DollarSign size={iconSize} />;
    case "credit-card":
      return <CreditCard size={iconSize} />;
    case "wallet":
      return <Wallet size={iconSize} />;
    case "other":
      return <Tag size={iconSize} />;
    case "book":
      return <Book size={iconSize} />;
    case "smartphone":
      return <Smartphone size={iconSize} />;
    default:
      return <Badge size={iconSize} />;
  }
};
