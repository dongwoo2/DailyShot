/**
 * v0 by Vercel.
 * @see https://v0.dev/t/0zGeW03vz26
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import Link from "next/link"


import {Input} from "../components/Input";
import Button from "../components/Button.";

export default function DailyMain() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="bg-[#ff8c00] text-primary-foreground py-4 px-6 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <Link href="#" className="flex items-center gap-2" prefetch={false}>
            <BoxIcon className="w-6 h-6" />
            <span className="text-lg font-bold">Sool</span>
          </Link>
          <nav className="hidden md:flex items-center gap-6">
            <Link href="#" className="hover:text-primary-foreground/80" prefetch={false}>
              History
            </Link>
            <Link href="#" className="hover:text-primary-foreground/80" prefetch={false}>
              Breweries
            </Link>
            <Link href="#" className="hover:text-primary-foreground/80" prefetch={false}>
              Types
            </Link>
            <Link href="#" className="hover:text-primary-foreground/80" prefetch={false}>
              Map
            </Link>
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <div className="relative flex-1 max-w-md">
            <SearchIcon className="absolute left-2 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input
              type="search"
              placeholder="Search products..."
              className="pl-8 pr-4 py-2 rounded-md bg-[#ff8c00]/20 focus:bg-[#ff8c00]/30 focus:outline-none"
            />
          </div>
          <Link href="#" className="hover:text-primary-foreground/80 flex items-center gap-2" prefetch={false}>
            <ShoppingCartIcon className="w-6 h-6" />
            <span>Cart</span>
          </Link>
          <Link href="#" className="hover:text-primary-foreground/80" prefetch={false}>
            <UserIcon className="w-6 h-6" />
          </Link>
        </div>
      </header>
      <main className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6 p-6">
        <div className="flex items-center justify-center md:col-span-1 md:flex-row-reverse gap-6">
          <img
            src="/placeholder.svg"
            alt="Makgeolli"
            width={800}
            height={600}
            className="w-full h-[300px] md:h-[400px] lg:h-[500px] object-cover rounded-lg"
          />
          <div className="flex-1 space-y-4">
            <h2 className="text-2xl font-bold">Explore Our Brewery Partners</h2>
            <Button variant="outline">Visit Breweries</Button>
          </div>
        </div>
        <div className="flex items-center justify-center md:col-span-1 md:flex-row gap-6">
          <img
            src="/placeholder.svg"
            alt="Makgeolli"
            width={800}
            height={600}
            className="w-full h-[300px] md:h-[400px] lg:h-[500px] object-cover rounded-lg"
          />
          <div className="flex-1 space-y-4">
            <h2 className="text-2xl font-bold">Discover the Flavors of Korea</h2>
            <Button variant="outline">Learn More</Button>
          </div>
        </div>
        <div className="relative group">
          <img
            src="/placeholder.svg"
            alt="Soju"
            width={800}
            height={600}
            className="w-full h-[300px] md:h-[400px] lg:h-[500px] object-cover rounded-lg"
          />
          <div className="absolute inset-0 bg-black/50 rounded-lg flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
            <h3 className="text-2xl font-bold text-primary-foreground">DailyShot!</h3>
          </div>
        </div>
      </main>
    </div>
  )
}

function BoxIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z" />
      <path d="m3.3 7 8.7 5 8.7-5" />
      <path d="M12 22V12" />
    </svg>
  )
}



function SearchIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="11" cy="11" r="8" />
      <path d="m21 21-4.3-4.3" />
    </svg>
  )
}


function ShoppingCartIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="8" cy="21" r="1" />
      <circle cx="19" cy="21" r="1" />
      <path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12" />
    </svg>
  )
}


function UserIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
      <circle cx="12" cy="7" r="4" />
    </svg>
  )
}