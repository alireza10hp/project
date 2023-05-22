from locust import task, run_single_user
from locust import FastHttpUser


class myharfile(FastHttpUser):
    host = "https://demo.guru99.com"

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/test/newtours/register.php",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://demo.guru99.com",
                "referer": "https://demo.guru99.com/test/newtours/register.php",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            },
            data="mercury=process&firstName=ali&lastName=alavi&phone=98991290q9546&userName=akbar%40tahoo.com&address1=tehran&city=tehran&state=tehran&postalCode=12434567&country=ALBANIA&email=ali&password=12345678&confirmPassword=12345678&submit=Submit",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/test/newtours/register_sucess.php",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "referer": "https://demo.guru99.com/test/newtours/register.php",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://securepubads.g.doubleclick.net/pagead/ppub_config?ippd=demo.guru99.com",
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(myharfile)
