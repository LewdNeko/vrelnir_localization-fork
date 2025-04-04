# Vrelnir Localization([Degrees of Lewdity](https://gitgud.io/Vrelnir/degrees-of-lewdity))
<a href='https://gitee.com/Number_Sir/vrelnir_localization/stargazers'><img src='https://gitee.com/Number_Sir/vrelnir_localization/badge/star.svg?theme=dark' alt='star'></img></a>
![GitHub stars](https://img.shields.io/github/stars/NumberSir/vrelnir_localization?style=social)

## Introduction
[Translation tool 0v0](https://github.com/NumberSir/vrelnir_localization)
1. Fetch the latest content from the original repository and download it locally
2. Generate the corresponding version dictionary and place it in the `raw_dict` folder
3. Download the latest localization package from `paratranz`. ((You may need to fill in your `token` in `.env`, which can be found in your personal settings).
4. Replace the automatically extracted localization package with the latest one, preserving invalid values.
5. Overwrite the game source files with the localization (checking for simple translation errors such as full-width commas: `"，`, or misaligned angle brackets: `<< >`)
6. Modify the version number to `chs-x.y.z`
7. Generate the localization dictionary package for `i18n` mod loading (default location: `data/json/i18n.json`)
8. Compile to `html` and run with the default browser (default location: `degrees-of-lewdity-master`)

## Usage
1. Requires Python 3.10+
2. Install dependencies via `cmd` or `shell` in root directory: `pip install -r requirements.txt`
3. Fill `.env` with your `token` (`PARATRANZ_TOKEN`), which can be found at `https://paratranz.cn/users/my`
4. Fill `.env` version number (`CHINESE_VERSION`)
5. Run `main.py` (via `cmd` or `shell` using `python -m main`)

## About Version Numbers
The Chinese localization version follows the format `chs-x.y.z`, e.g., `chs-alpha1.7.1`

The full game version format is `{游戏版本号}-chs-{汉化版本号}`, e.g., `0.4.1.7-chs-alpha1.7.1`

Localization versioning follows these rules:
1. `alpha` / `beta` / `release` represent:
   - `alpha`: Current translation is 100% complete, but may contain missing extracted texts or unpolished translations.
   - `beta`: Current translation is 100% complete, no missing extracted texts, but still unpolished.
   - `release`: Current translation is 100% complete, no missing extracted texts, and fully polished.
2. If the game undergoes a major update：e.g., `0.4.1` => `0.4.2`, or `0.4` -> `0.5`, the localization version resets, for example:
   - `0.4.1.7-chs-alpha1.7.1` => `0.4.2.4-chs-alpha1.0.0`
3. If the game receives minor updates：e.g., `0.4.1.6` => `0.4.1.7`, or `0.4.2.0` => `0.4.2.5`, the first digit in the localization version increments, for example:
   - `0.4.2.4-chs-alpha1.0.0` => `0.4.2.5-chs-alpha2.0.0`
4. Weekly updates on Friday at 9 PM increase the second digit, for example:
   - `0.4.1.7-chs-alpha1.6.0` => `0.4.1.7-chs-alpha1.7.0`
5. If a critical bug preventing game progress is fixed, the last digit increments, for example:
   - `0.4.1.7-chs-alpha1.7.0` => `0.4.1.7-chs-alpha1.7.1`
6. If packaging a private/internal preview version, append `-pre`，to the localization version, for example:
   - `0.4.1.7-chs-alpha1.7.1` => `0.4.1.7-chs-alpha1.8.0-pre` 