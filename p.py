# DEBUG PRACTITIONER PAGINATION

url = f"{FHIR_BASE}/Practitioner?active=true"

for page in range(1, 6):  # check first 5 pages only

    print("\n" + "="*50)
        print(f"PAGE {page}")
            print("="*50)

                response = call_api(url)

                    print("Status Code:", response.status_code)

                        if response.status_code != 200:
                                print(response.text[:1000])
                                        break

                                            bundle = response.json()

                                                entries = bundle.get("entry", [])

                                                    print("Records on page:", len(entries))

                                                        print("\nRelations found:")

                                                            next_url = None

                                                                for link in bundle.get("link", []):

                                                                        relation = link.get("relation")

                                                                                print(" -", relation)

                                                                                        if relation == "next":
                                                                                                    next_url = link.get("url")

                                                                                                        print("\nNext URL exists:", next_url is not None)

                                                                                                            if next_url:
                                                                                                                    print("First 150 chars of next URL:")
                                                                                                                            print(next_url[:150])

                                                                                                                                if not next_url:
                                                                                                                                        print("\nNO MORE PAGES")
                                                                                                                                                break

                                                                                                                                                    url = next_url