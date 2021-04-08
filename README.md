# rust_issues_83925

## 测试

```bash
cargo bisect-rustc --script=/home/light4/playground/rust_issues_83925/check.py --test-dir=foo \
    --start=2020-10-08 \
    --end=2021-02-11 \
    --target=thumbv7em-none-eabi \
    --preserve \
    -vvvvv
```

## 结果

```plain
Regression in nightly-2020-10-17
```
