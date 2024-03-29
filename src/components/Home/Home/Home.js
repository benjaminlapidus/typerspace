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
  const [link, setLink] = React.useState("");
  const ytParser = (url) => {
    var regExp =
      /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    setLink(match && match[7].length == 11 ? match[7] : false);
  };
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
                <a href="http://127.0.0.1:5000/" className="font-medium">
                  Log in
                </a>
              </div>
            </nav>
          </div>

          <main className="gap-4 mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
            <div className="md:text-left md:max-w-xl">
              <h1 className="text-3xl sm:text-4xl tracking-tight font-extrabold text-gray-900 dark:text-gray-100 md:text-7xl">
                <span className="font-mono block xl:inline">
                  typer
                  <span className=" text-purple-800 dark:text-purple-300">
                    space
                  </span>
                </span>
              </h1>
              <div className="md:pl-3">
                <p className="m-2 text-base text-gray-500 dark:text-gray-300 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl">
                  Learning to type doesn't have to be boring. Practice typing
                  using your favorite videos and songs.
                </p>
                <form className="Home__form" action={"/dashboard"}>
                  <div className="my-2">
                    <label className="block dark:text-gray-400">
                      YouTube URL
                    </label>
                    <input
                      type="text"
                      placeholder="Placeholder"
                      onChange={(e) => ytParser(e.target.value)}
                      type="text"
                      name="link"
                      className="px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white bg-white rounded text-sm border-0 shadow outline-none focus:outline-none focus:ring"
                    />
                  </div>

                  <div className="Home__submitButtonWrapper">
                    <input
                      id="Home__submitButton"
                      type="submit"
                      value="take off"
                    />
                  </div>
                </form>
              </div>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

export default Home;
