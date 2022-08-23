def parse():
    results = {}
    with open('timestamps', mode='r') as ts_file:
        for line in ts_file:
            content = line[:-1].split("|")
            cid = content[2]
            timestamp = content[0]
            if cid in results:
                result_list = results[cid]
                result_list.append(timestamp)
                result_list.append(f'{float((int(timestamp) - int(result_list[1])) / 3600):.2f}')
                result_list.append(content[3])
                result_list.append(content[4])
            else:
                results[cid] = [cid, timestamp]

    with open('outputs_ali1.csv', mode='w+') as output:
        output.write('cid, beginning, end, hours_connected, status_code, error_code\n')
        for key in results.keys():
            output.write(','.join(str(e) for e in results[key]))
            output.write('\n')


if __name__ == '__main__':
    parse()
