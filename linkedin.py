#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import pandas as pd
from datetime import datetime, timedelta
import requests
import random
import time
import json
from html import unescape
from threading import Thread, Event
from bs4 import BeautifulSoup
import os
import sys
import subprocess
import geonamescache
from tkinter import PhotoImage
import concurrent.futures

def get_random_user_agent():
    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.192.400 QQBrowser/11.5.5250.400',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
    'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
    ]
    return random.choice(user_agents)

def get_random_proxy():
    proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text'
    proxy_response = requests.get(proxy_list_url)
    proxy_list = proxy_response.text.splitlines()
    return {'http': 'http://' + random.choice(proxy_list)}

def country_list():
    return {
        'AF': 'Afghanistan',
        'AX': 'Åland Islands',
        'AL': 'Albania',
        'DZ': 'Algeria',
        'AS': 'American Samoa',
        'AD': 'Andorra',
        'AO': 'Angola',
        'AI': 'Anguilla',
        'AQ': 'Antarctica',
        'AG': 'Antigua and Barbuda',
        'AR': 'Argentina',
        'AM': 'Armenia',
        'AW': 'Aruba',
        'AU': 'Australia',
        'AT': 'Austria',
        'AZ': 'Azerbaijan',
        'BS': 'Bahamas',
        'BH': 'Bahrain',
        'BD': 'Bangladesh',
        'BB': 'Barbados',
        'BY': 'Belarus',
        'BE': 'Belgium',
        'BZ': 'Belize',
        'BJ': 'Benin',
        'BM': 'Bermuda',
        'BT': 'Bhutan',
        'BO': 'Bolivia',
        'BQ': 'Bonaire, Sint Eustatius and Saba',
        'BA': 'Bosnia and Herzegovina',
        'BW': 'Botswana',
        'BV': 'Bouvet Island',
        'BR': 'Brazil',
        'IO': 'British Indian Ocean Territory',
        'BN': 'Brunei Darussalam',
        'BG': 'Bulgaria',
        'BF': 'Burkina Faso',
        'BI': 'Burundi',
        'CV': 'Cabo Verde',
        'KH': 'Cambodia',
        'CM': 'Cameroon',
        'CA': 'Canada',
        'KY': 'Cayman Islands',
        'CF': 'Central African Republic',
        'TD': 'Chad',
        'CL': 'Chile',
        'CN': 'China',
        'CX': 'Christmas Island',
        'CC': 'Cocos (Keeling) Islands',
        'CO': 'Colombia',
        'KM': 'Comoros',
        'CG': 'Congo',
        'CD': 'Congo, Democratic Republic of the',
        'CK': 'Cook Islands',
        'CR': 'Costa Rica',
        'CI': 'Côte d\'Ivoire',
        'HR': 'Croatia',
        'CU': 'Cuba',
        'CW': 'Curaçao',
        'CY': 'Cyprus',
        'CZ': 'Czech Republic',
        'DK': 'Denmark',
        'DJ': 'Djibouti',
        'DM': 'Dominica',
        'DO': 'Dominican Republic',
        'EC': 'Ecuador',
        'EG': 'Egypt',
        'SV': 'El Salvador',
        'GQ': 'Equatorial Guinea',
        'ER': 'Eritrea',
        'EE': 'Estonia',
        'ET': 'Ethiopia',
        'FK': 'Falkland Islands (Malvinas)',
        'FO': 'Faroe Islands',
        'FJ': 'Fiji',
        'FI': 'Finland',
        'FR': 'France',
        'GF': 'French Guiana',
        'PF': 'French Polynesia',
        'TF': 'French Southern Territories',
        'GA': 'Gabon',
        'GM': 'Gambia',
        'GE': 'Georgia',
        'DE': 'Germany',
        'GH': 'Ghana',
        'GI': 'Gibraltar',
        'GR': 'Greece',
        'GL': 'Greenland',
        'GD': 'Grenada',
        'GP': 'Guadeloupe',
        'GU': 'Guam',
        'GT': 'Guatemala',
        'GG': 'Guernsey',
        'GN': 'Guinea',
        'GW': 'Guinea-Bissau',
        'GY': 'Guyana',
        'HT': 'Haiti',
        'HM': 'Heard Island and McDonald Islands',
        'VA': 'Holy See',
        'HN': 'Honduras',
        'HK': 'Hong Kong',
        'HU': 'Hungary',
        'IS': 'Iceland',
        'IN': 'India',
        'ID': 'Indonesia',
        'IR': 'Iran, Islamic Republic of',
        'IQ': 'Iraq',
        'IE': 'Ireland',
        'IM': 'Isle of Man',
        'IL': 'Israel',
        'IT': 'Italy',
        'JM': 'Jamaica',
        'JP': 'Japan',
        'JE': 'Jersey',
        'JO': 'Jordan',
        'KZ': 'Kazakhstan',
        'KE': 'Kenya',
        'KI': 'Kiribati',
        'KP': 'Korea, Democratic People\'s Republic of',
        'KR': 'Korea, Republic of',
        'KW': 'Kuwait',
        'KG': 'Kyrgyzstan',
        'LA': 'Lao People\'s Democratic Republic',
        'LV': 'Latvia',
        'LB': 'Lebanon',
        'LS': 'Lesotho',
        'LR': 'Liberia',
        'LY': 'Libya',
        'LI': 'Liechtenstein',
        'LT': 'Lithuania',
        'LU': 'Luxembourg',
        'MO': 'Macao',
        'MK': 'North Macedonia',
        'MG': 'Madagascar',
        'MW': 'Malawi',
        'MY': 'Malaysia',
        'MV': 'Maldives',
        'ML': 'Mali',
        'MT': 'Malta',
        'MH': 'Marshall Islands',
        'MQ': 'Martinique',
        'MR': 'Mauritania',
        'MU': 'Mauritius',
        'YT': 'Mayotte',
        'MX': 'Mexico',
        'FM': 'Micronesia, Federated States of',
        'MD': 'Moldova, Republic of',
        'MC': 'Monaco',
        'MN': 'Mongolia',
        'ME': 'Montenegro',
        'MS': 'Montserrat',
        'MA': 'Morocco',
        'MZ': 'Mozambique',
        'MM': 'Myanmar',
        'NA': 'Namibia',
        'NR': 'Nauru',
        'NP': 'Nepal',
        'NL': 'Netherlands',
        'NC': 'New Caledonia',
        'NZ': 'New Zealand',
        'NI': 'Nicaragua',
        'NE': 'Niger',
        'NG': 'Nigeria',
        'NU': 'Niue',
        'NF': 'Norfolk Island',
        'MP': 'Northern Mariana Islands',
        'NO': 'Norway',
        'OM': 'Oman',
        'PK': 'Pakistan',
        'PW': 'Palau',
        'PS': 'Palestine, State of',
        'PA': 'Panama',
        'PG': 'Papua New Guinea',
        'PY': 'Paraguay',
        'PE': 'Peru',
        'PH': 'Philippines',
        'PN': 'Pitcairn',
        'PL': 'Poland',
        'PT': 'Portugal',
        'PR': 'Puerto Rico',
        'QA': 'Qatar',
        'RE': 'Réunion',
        'RO': 'Romania',
        'RU': 'Russian Federation',
        'RW': 'Rwanda',
        'BL': 'Saint Barthélemy',
        'SH': 'Saint Helena, Ascension and Tristan da Cunha',
        'KN': 'Saint Kitts and Nevis',
        'LC': 'Saint Lucia',
        'MF': 'Saint Martin (French part)',
        'PM': 'Saint Pierre and Miquelon',
        'VC': 'Saint Vincent and the Grenadines',
        'WS': 'Samoa',
        'SM': 'San Marino',
        'ST': 'Sao Tome and Principe',
        'SA': 'Saudi Arabia',
        'SN': 'Senegal',
        'RS': 'Serbia',
        'SC': 'Seychelles',
        'SL': 'Sierra Leone',
        'SG': 'Singapore',
        'SX': 'Sint Maarten (Dutch part)',
        'SK': 'Slovakia',
        'SI': 'Slovenia',
        'SB': 'Solomon Islands',
        'SO': 'Somalia',
        'ZA': 'South Africa',
        'GS': 'South Georgia and the South Sandwich Islands',
        'SS': 'South Sudan',
        'ES': 'Spain',
        'LK': 'Sri Lanka',
        'SD': 'Sudan',
        'SR': 'Suriname',
        'SJ': 'Svalbard and Jan Mayen',
        'SZ': 'Swaziland',
        'SE': 'Sweden',
        'CH': 'Switzerland',
        'SY': 'Syrian Arab Republic',
        'TW': 'Taiwan, Province of China',
        'TJ': 'Tajikistan',
        'TZ': 'Tanzania, United Republic of',
        'TH': 'Thailand',
        'TL': 'Timor-Leste',
        'TG': 'Togo',
        'TK': 'Tokelau',
        'TO': 'Tonga',
        'TT': 'Trinidad and Tobago',
        'TN': 'Tunisia',
        'TR': 'Turkey',
        'TM': 'Turkmenistan',
        'TC': 'Turks and Caicos Islands',
        'TV': 'Tuvalu',
        'UG': 'Uganda',
        'UA': 'Ukraine',
        'AE': 'United Arab Emirates',
        'GB': 'United Kingdom',
        'US': 'United States',
        'UM': 'United States Minor Outlying Islands',
        'UY': 'Uruguay',
        'UZ': 'Uzbekistan',
        'VU': 'Vanuatu',
        'VE': 'Venezuela, Bolivarian Republic of',
        'VN': 'Viet Nam',
        'VG': 'Virgin Islands, British',
        'VI': 'Virgin Islands, U.S.',
        'WF': 'Wallis and Futuna',
        'EH': 'Western Sahara',
        'YE': 'Yemen',
        'ZM': 'Zambia',
        'ZW': 'Zimbabwe'
    }

def get_job(job_id, job_link, console_log, use_proxy=False):
    max_retries = 5
    retries = 0
    use_proxy = False

    while retries < max_retries:
        try:
            headers = {'User-Agent': get_random_user_agent()}
            proxies = get_random_proxy() if use_proxy else None

            response = requests.get(
                f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}",
                headers=headers,
                proxies=proxies
            )
            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            posted_time_ago = soup.select_one(".posted-time-ago__text").text.strip()
            number_of_applicants = soup.select_one(".num-applicants__caption").text.strip()
            
            job_description_html = soup.select_one(".show-more-less-html__markup").decode_contents()
            job_description = BeautifulSoup(job_description_html, 'html.parser').get_text("\n", strip=True)

            company = soup.select_one(".topcard__org-name-link").text.strip()
            location = soup.select_one(".topcard__flavor--bullet").text.strip().replace("\n", "")
            title = soup.select_one(".topcard__title").text.strip()

            criteria = soup.select(".description__job-criteria-item")
            criteria_dict = {
                item.select_one(".description__job-criteria-subheader").text.strip(): 
                item.select_one(".description__job-criteria-text--criteria").text.strip()
                for item in criteria
            }
            console_log.insert(tk.END, f"==>: {title} at {company}, location: {location}\n")
            return {
                "title": title,
                "company": company,
                "location": location,
                "link": job_link,
                "postedTimeAgo": posted_time_ago,
                "numberOfApplicants": number_of_applicants,
                "description": job_description,
                **criteria_dict
            }
        except requests.ConnectionError as e:
            console_log.insert(tk.END, f"Connection error: {e}\n")
            time.sleep(random.uniform(2, 5))
        except requests.HTTPError as e:
            if e.response.status_code == 403 or e.response.status_code == 429:
                use_proxy = True
                retries += 1
                time.sleep(random.uniform(2, 5))
            else:
                console_log.insert(tk.END, f"HTTP error: {e}\n")
                break
        except Exception as e:
            console_log.insert(tk.END, f"Error getting job: {e}\n")
            time.sleep(random.uniform(2, 5))
            break

def scrape_linkedin_jobs(filter_type, keyword, location, city, console_log, stop_event):

    if filter_type == 'past_month':
        time_filter = '&f_TPR=r2592000'
    elif filter_type == 'past_week':
        time_filter = '&f_TPR=r604800'
    elif filter_type == 'past_24_hours':
        time_filter = '&f_TPR=r86400'
    else:  # 'any_time'
        time_filter = ''

    all_jobs = []
    page = 1
    location_query = f"{city}, {location}" if city else location

    while True:
        max_retries = 5
        retries = 0
        use_proxy = False

        while retries < max_retries:
            try:
                offset = (page - 1) * 25
                headers = {'User-Agent': get_random_user_agent()}
                proxies = get_random_proxy() if use_proxy else None

                response = requests.get(
                    f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location_query}{time_filter}&start={offset}",
                    headers=headers,
                    proxies=proxies
                )
                response.raise_for_status()
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                page_jobs = soup.select(".job-search-card")

                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                    future_to_job_details = {
                        executor.submit(get_job, job.get("data-entity-urn").split(":")[-1], job.find('a', class_='base-card__full-link')['href'].strip(), console_log): job
                        for job in page_jobs
                    }

                    for future in concurrent.futures.as_completed(future_to_job_details):
                        if stop_event.is_set():
                            console_log.insert(tk.END, f"Stopping Scraping...\n")
                            return all_jobs
                        job_details = future.result()
                        if job_details:
                            all_jobs.append(job_details)
                
                if not len(page_jobs):
                    return all_jobs
                else:
                    console_log.insert(tk.END, f"Scraped {len(page_jobs)} jobs from page {page}\n")    
                break
            except requests.ConnectionError as e:
                console_log.insert(tk.END, f"Connection error: {e}\n")
                time.sleep(random.uniform(2, 5))
            except requests.HTTPError as e:
                if e.response.status_code == 403 or e.response.status_code == 429:
                    use_proxy = True
                    retries += 1
                    time.sleep(random.uniform(2, 5))
                elif e.response.status_code == 400:
                    return all_jobs
            except Exception as e:
                retries += 1
                time.sleep(random.uniform(2, 5))

        page += 1
        time.sleep(random.uniform(1, 3))
    return all_jobs

def save_to_excel(jobs, output_file, console_log):
    df = pd.DataFrame(jobs)
    df.to_excel(output_file, index=False)
    console_log.insert(tk.END, f"Data saved successfully.\n")

def start_scraping(filter_type, keyword, location, city, output_file, console_log, stop_event):
    console_log.delete(1.0, tk.END)
    if not keyword or not output_file:
        messagebox.showerror("Input Error", "Keyword and Output File are required.")
        return

    console_log.insert(tk.END, "Starting job scraping...\n")
    jobs = scrape_linkedin_jobs(filter_type, keyword, location, city, console_log, stop_event)
    if jobs:
        save_to_excel(jobs, output_file, console_log)
    console_log.insert(tk.END, f"Scraped {len(jobs)} jobs and saved to {output_file}\n")

def browse_file(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def open_file(entry):
    file_path = entry.get()
    if file_path and os.path.exists(file_path):
        if os.name == 'nt':  # For Windows
            os.startfile(file_path)
        elif os.name == 'posix':
            if sys.platform == 'darwin':  # macOS
                subprocess.call(["open", file_path])
            else:  # Linux and other Unix-like systems
                subprocess.call(["xdg-open", file_path])
    else:
        messagebox.showerror("File Error", "File not found or path is invalid.")

class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list

    def autocomplete(self, delta=0):
        if delta:  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts from there
            self.position = len(self.get())

        _hits = []
        for item in self._completion_list:
            if item.lower().startswith(self.get().lower()):
                _hits.append(item)

        if _hits != self._hits:
            self._hits = _hits
            self._hit_index = 0

        if _hits:
            self._hits = _hits
            self._hit_index = (self._hit_index + delta) % len(_hits)
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
            return
        self.autocomplete()


def update_cities(event):
    selected_country = location_combo.get()
    country_code = [code for code, name in countries.items() if name == selected_country][0]

    gc = geonamescache.GeonamesCache()
    all_cities = gc.get_cities()

    city_names = [city_data['name'] for city_id, city_data in all_cities.items() if city_data['countrycode'] == country_code]
    city_names.sort()
    
    city_combo.set_completion_list(city_names)



def create_gui():
    global location_combo, city_combo, countries, gc

    root = tk.Tk()
    root.title("LinkedIn Job Scraper")

    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Keyword:").grid(row=0, column=0, sticky=tk.W)
    keyword_entry = ttk.Entry(mainframe, width=50)
    keyword_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Date Range:").grid(row=1, column=0, sticky=tk.W)
    filter_combo = ttk.Combobox(mainframe, width=47, state='readonly')
    filter_combo['values'] = ('any_time', 'past_month', 'past_week', 'past_24_hours')
    filter_combo.grid(row=1, column=1, sticky=(tk.W, tk.E))
    filter_combo.current(0)

    ttk.Label(mainframe, text="Country:").grid(row=2, column=0, sticky=tk.W)



    countries = country_list()

    country_names = list(countries.values())
    country_names = sorted(country_names)
    country_names.sort()
    country_names.insert(0, "India")
    location_combo = ttk.Combobox(mainframe, width=47, state='readonly', values=country_names)
    location_combo.grid(row=2, column=1, sticky=(tk.W, tk.E))
    location_combo.current(0)
    location_combo.bind('<<ComboboxSelected>>', update_cities)

    ttk.Label(mainframe, text="City:").grid(row=3, column=0, sticky=tk.W)
    city_combo = AutocompleteCombobox(mainframe, width=47)
    city_combo.grid(row=3, column=1, sticky=(tk.W, tk.E))

    stop_event = Event()
    search_button = ttk.Button(mainframe, text="Search", command=lambda: Thread(target=start_scraping, args=(filter_combo.get(), keyword_entry.get(), location_combo.get(), city_combo.get(), output_entry.get(), console_log, stop_event)).start())
    search_button.grid(row=4, column=1, sticky=tk.E, pady=10)

    stop_button = ttk.Button(mainframe, text="Stop & Save", command=lambda: stop_event.set())
    stop_button.grid(row=4, column=0, sticky=tk.W, pady=10)

    console_log = scrolledtext.ScrolledText(mainframe, wrap=tk.WORD)
    console_log.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    browse_frame = ttk.Frame(mainframe)
    browse_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Label(browse_frame, text="Export to:").grid(row=0, column=0, sticky=tk.W)
    output_entry = ttk.Entry(browse_frame, width=50)
    output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    browse_button = ttk.Button(browse_frame, text="Browse", command=lambda: browse_file(output_entry))
    browse_button.grid(row=0, column=2, sticky=tk.W, padx=5)

    open_with = ttk.Button(mainframe, text="Open", command=lambda: open_file(output_entry))
    open_with.grid(row=7, column=1, sticky=tk.E, pady=10)   

    retry_button = ttk.Button(mainframe, text="Retry", command=lambda: Thread(target=start_scraping, args=(filter_combo.get(), keyword_entry.get(), location_combo.get(), city_combo.get(), output_entry.get(), console_log, Event())).start())
    retry_button.grid(row=7, column=0, sticky=tk.W, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.rowconfigure(5, weight=1)

    gc = geonamescache.GeonamesCache()

    basedir = os.path.dirname(os.path.abspath(__file__))

    icon_file = os.path.join(basedir, "linkedin.ico")
    if os.path.exists(icon_file):
        try:
            # Try setting the icon using the platform-specific method
            if os.name == 'nt':  # Windows
                root.iconbitmap(icon_file)
            elif sys.platform == 'darwin':  # macOS
                icon_image = PhotoImage(file=icon_file)
                root.iconphoto(True, icon_image)
            else:  # Linux
                icon_file = os.path.join(basedir, "linkedin.png")
                icon_image = PhotoImage(file=icon_file)
                root.iconphoto(True, icon_image)
        except tk.TclError:
            print("Failed to set icon. Continuing without icon.")
    else:
        print("Icon file not found:", icon_file)


    root.mainloop()

if __name__ == '__main__':
    create_gui()
