def calculate_royalties(company, works, month):
    total_tax = 0
    report = []

    profit = company.monthly_profits.get(month, 0)
    royalty_pool = profit * company.royalty_percent()

    for work in works:
        for author, share in work.authors_shares.items():
            royalty = royalty_pool * share
            tax = calculate_tax(author, royalty)
            total_tax += tax
            report.append({
                'author': author.full_name,
                'royalty': royalty,
                'tax': tax,
                'net_income': royalty - tax
            })

    return report, total_tax


def calculate_tax(author, amount):
    if author.is_resident:
        return amount * 0.20
    else:
        if amount <= 1000:
            return amount * 0.02
        elif amount <= 5000:
            return amount * 0.05
        elif amount <= 10000:
            return amount * 0.10
        elif amount <= 20000:
            return amount * 0.15
        elif amount <= 50000:
            return amount * 0.20
        else:
            return amount * 0.25
