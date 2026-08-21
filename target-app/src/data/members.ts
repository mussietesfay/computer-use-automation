export interface Member {
  id: string;
  name: string;
  status: "Active" | "Inactive";
  email: string;
  savingsBalance: number;
}

export const members: Member[] = [
  {
    id: "12345",
    name: "John Smith",
    status: "Active",
    email: "john@example.com",
    savingsBalance: 12450,
  },
  {
    id: "67890",
    name: "Jane Doe",
    status: "Active",
    email: "jane@example.com",
    savingsBalance: 8750,
  },
  {
    id: "54321",
    name: "Michael Brown",
    status: "Inactive",
    email: "michael@example.com",
    savingsBalance: 3200,
  },
];