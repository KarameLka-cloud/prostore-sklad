import {ReactNode} from "react";

export default function AuthLayout({children}: { children: ReactNode }) {
    return (
        <div>
            <header>Auth layout</header>
            {children}
        </div>
    )
}
