import React from "react";
import "./Home.css";

import { Fragment } from "react";
import { Popover, Transition } from "@headlessui/react";
import { MenuIcon, XIcon } from "@heroicons/react/outline";

const navigation = [
  { name: "Product", href: "#" },
  { name: "Features", href: "#" },
  { name: "Marketplace", href: "#" },
  { name: "Company", href: "#" },
];

function Home(props) {
  return (
    <div className="relative bg-white dark:bg-gray-900 overflow-hidden">
      <div className="max-w-7xl mx-auto">
        <div className="relative h-screen z-10 pb-8 bg-white dark:bg-gray-900 sm:pb-16 md:pb-20  lg:w-full lg:pb-28 xl:pb-32">
          <div className="relative pt-6 px-4 sm:px-6 lg:px-8">
            <nav
              className="relative flex items-center justify-between sm:h-10"
              aria-label="Global"
            >
              <div className="flex items-center flex-grow flex-shrink-0 lg:flex-grow-0">
                <div className="flex items-center justify-between w-full md:w-auto">
                  <a href="#">
                    <span className="sr-only">Workflow</span>
                    <img
                      className="h-8 w-auto sm:h-10"
                      src="https://tailwindui.com/img/logos/workflow-mark-purple-600.svg"
                    />
                  </a>
                </div>
              </div>
              <div className="block md:ml-10 md:space-x-8 rounded bg-purple-800 hover:bg-purple-700 px-3 py-2 text-center text-gray-100">
                <a href="http://127.0.0.1:5000/login" className="font-medium">
                  Log in
                </a>
              </div>
            </nav>
          </div>

          <main className="grid grid-cols-12 gap-4 mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
            <div className="col-start-2 col-span-10 sm:text-center">
              <h1 className="text-6xl tracking-tight font-extrabold text-gray-900 dark:text-gray-100 sm:text-6xl md:text-9xl">
                <span className="font-mono block xl:inline">typerspace</span>
              </h1>
              <p className="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                Learning to type doesn't have to be boring. Practice while
                typing alongside your favorite videos and songs.
              </p>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

export default Home;
