# Appium Client Side + Webdriver.io

This directory contains simple test scenario using
[Appium](http://appium.io/) + [Webdriver.io](https://webdriver.io/) + [Mocha](https://mochajs.org/).

Note: For now it's Android only example.

## Structure

```sh
.
├── package.json
├── package-lock.json
├── screenshots
│   └── .gitkeep
├── test
│   └── specs
│       └── main.js
└── wdio.conf.js
```

* `package.json` and `package-lock.json` is obvious for everyone familiar with Node.js. Shortly for those who doesn't know:
it contains information about project and what's more important - dependenencies.
* `screenshots` - Here will appear all taken screenshots. Note: Directory will be cleared before each test run.
* `test/specs/main.js` - Test itself
* `wdio.conf.js` - Config for [Webdriver.io Testrunner](https://webdriver.io/docs/gettingstarted.html)

### Dependencies

* `@wdio/cli` - Webdriver.io (and Testrunner)
* `@wdio/local-runner` - To run test "locally" (because from server perspective it's locally)
* `@wdio/mocha-framework` - Mocha support
* `@wdio/spec-reporter` - Default [spec reporter](https://webdriver.io/docs/spec-reporter.html)
* `@wdio/sync` - To be able to enable [sync mode](https://webdriver.io/docs/sync-vs-async.html)
* `chai` - Chai for Mocha (because I wanted to use [should](https://www.chaijs.com/guide/styles/#should) [BDD style])

## Usage

### Install Dependencies

```sh
npm ci
```

### Prepare Webdriver.io Configuration

You need to edit `wdio.conf.js` and set capabilities. You can either edit existing one (if you set API key then it should
work out of the box) or you can use [Capabilities Creator](https://bitbar.github.io/capabilities-creator/) (you just need
to switch mode to "Appium" and in top right corner language to "Node.js").

### Run

```sh
npm run test
```

## FAQ

> To use Chai's `should` you need to run proper code. Where it's done?

It's in `wdio.conf.js`'s `before` hook.

> There is global function `takeScreenshot` in test - where it came from?

It's in `wdio.conf.js`'s `before` hook.

## Links

* [Webdriver.io Testrunner Configuration](https://webdriver.io/docs/configurationfile.html) (helpful if you want to understand and modify `wdio.conf.js`)
* [Webdriver.io Appium API](https://webdriver.io/docs/api/appium.html)
* [Chai BDD API](https://www.chaijs.com/api/bdd/)
